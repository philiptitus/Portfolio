import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

console.clear();

// load fonts
await (async function () {
  async function loadFont(fontface) {
    await fontface.load();
    document.fonts.add(fontface);
  }
  let fonts = [
    new FontFace(
      "Neonderthaw",
      "url(https://fonts.gstatic.com/s/neonderthaw/v6/Iure6Yx5-oWVZI0r-17AeaZOrLQ.woff2)"
    ),
    new FontFace(
      "TiltNeon",
      "url(https://fonts.gstatic.com/s/tiltneon/v10/E21L_d7gguXdwD9LEFY2WCeElCNtd-eBqpHp1TzrkJSmwpj5ndxquUK6UOc.woff2)"
    ),
    new FontFace(
      "Michroma",
      "url(https://fonts.gstatic.com/s/michroma/v19/PN_zRfy9qWD8fEagAPg9pTk.woff2)"
    )
  ];
  for (let font in fonts) {
    //console.log(fonts[font]);
    await loadFont(fonts[font]);
  }
})();

class FloorBase extends THREE.Mesh {
  constructor() {    
    let hfs = 50; // half floor size
    let hhs = 5; // half hole size;
    let floorShape = new THREE.Shape(
      [
        [hfs, hfs],
        [hfs, -hfs],
        [-hfs, -hfs],
        [-hfs, hfs]
      ].map((p) => {
        return new THREE.Vector2(p[0], p[1]);
      })
    );
    let floorHole = new THREE.Path()
      .moveTo(hhs, hhs)
      .lineTo(hhs, -hhs)
      .lineTo(-hhs, -hhs)
      .lineTo(-hhs, hhs)
      .lineTo(hhs, hhs);
    floorShape.holes.push(floorHole);
    super();
    this.camPosition = {value: new THREE.Vector3()};
    this.geometry = new THREE.ShapeGeometry(floorShape).rotateX(Math.PI * -0.5);
    this.material = new THREE.MeshStandardMaterial({
      onBeforeCompile: shader => {
        shader.uniforms.camPosition = this.camPosition;
        shader.uniforms.textTexture = {value: getTexture()};
        shader.vertexShader = `
          uniform vec3 camPosition;
          varying vec3 vPos;
          mat2 rot2d(float a){return mat2(cos(a), sin(a), -sin(a), cos(a));}
          ${shader.vertexShader}
        `.replace(
          `#include <begin_vertex>`,
          `#include <begin_vertex>
            float a = atan(camPosition.z, camPosition.x) - PI * 0.375;
            float hPI = PI * 0.5;
            a = floor(a / hPI) * hPI; 
            vPos = position;
            vPos.xz *= rot2d(a);
          `
        );
        //console.log(shader.vertexShader);
        shader.fragmentShader = `
          uniform sampler2D textTexture;
          varying vec3 vPos;
          ${shader.fragmentShader}
        `.replace(
          `#include <map_fragment>`,
          `
            float patchW = 7.;
            float patchH = patchW / 8.;
            vec2 patchC = vec2(-1.5, 5. + patchH * 0.5);
            vec2 uv = (vPos.xz - (patchC + vec2(-patchW, -patchH) * 0.5)) / vec2(patchW, patchH);
            uv.y = 1. - uv.y;
            
            vec4 sampledDiffuseColor = texture2D( textTexture, uv );
            diffuseColor *= sampledDiffuseColor;
          
          `
        );
        //console.log(shader.fragmentShader);
      }
    });
    
    
    function getTexture(){
      let c = document.createElement("canvas");
      c.width = 1024;
      c.height = 128;
      
      let ctx = c.getContext("2d");
          ctx.fillStyle = "#fff";
          ctx.fillRect(0, 0, c.width, c.height);
          
          ctx.font = `${c.height * 0.5}px Michroma`;
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          
          ctx.fillStyle = "#444";
          ctx.fillText("849 # Noisy ribbons", c.width * 0.5, c.height * 0.5);
      
      let texture = new THREE.CanvasTexture(c);
          texture.colorSpace = THREE.SRGBColorSpace;
      
      return texture;
          
    }
  }
  
  update(camera){
    this.worldToLocal(this.camPosition.value.copy(camera.position));
  }
}

class Ribbons extends THREE.Mesh {
  constructor(gu, amount) {
    let totalSize = 10;
    let g = new THREE.InstancedBufferGeometry().copy(
      new THREE.PlaneGeometry(1, 1, 200, 1)
        .translate(0, 0.5, 0)
        .rotateX(Math.PI * -0.5)
    );
    g.instanceCount = amount;
    
    let getHeight = `
          float getHeight(vec3 data){
            float amp = 10.;
            float freq = 0.25;
            data.x *= freq;
            float n = snoise(data);
            return n * n * amp;
          }`;
    let compute = `
    
            float stripeWidth = ${totalSize}. / ${amount}.;
            float iID = float(gl_InstanceID);
            
            vec3 pos = vec3(position);
            
            pos.xz *= vec2(${totalSize}., stripeWidth);
            float zPos = 5. - stripeWidth * iID;
            pos.z += zPos;
            
            float lenRatio = smoothstep(4.9, 1., abs(pos.x));
            float wdtRatio = 0.1 + smoothstep(5., 1., abs(zPos - stripeWidth * 0.5)) * 0.5;
            
            float t = time * 0.25;
            float t2 = time * 0.5;
            
            float h = getHeight(vec3(pos.x + t2, zPos * 0.25, t));
            h *= lenRatio * wdtRatio;
            pos.y = h;
    `;
    let m = new THREE.MeshStandardMaterial({
      //wireframe: true,
      side: THREE.DoubleSide,
      onBeforeCompile: (shader) => {
        shader.uniforms.time = gu.time;
        shader.vertexShader = `
          uniform float time;
          ${noise}
          ${getHeight}
          
          ${shader.vertexShader}
        `.replace(
          `#include <beginnormal_vertex>`,
          `#include <beginnormal_vertex>
          
            ${compute}
            
            float h2 = getHeight(vec3(pos.x + t2 + 0.1, zPos * 0.25, t));
            h2 *= lenRatio * wdtRatio;
            objectNormal = normalize(vec3(h - h2, 0.1, 0.));
            
            
          `
        ).replace(
            `#include <begin_vertex>`,
            `#include <begin_vertex>
            
            transformed = pos;
          `
          );
        //console.log(shader.vertexShader);
      }
    });
    super(g, m);
    this.customDepthMaterial = new THREE.MeshDepthMaterial({
      depthPacking: THREE.RGBADepthPacking,
      side: THREE.DoubleSide,
      onBeforeCompile: shader => {
        shader.uniforms.time = gu.time;
        shader.vertexShader = `
          uniform float time;
          ${noise}
          ${getHeight}
          
          ${shader.vertexShader}
        `.replace(
          `#include <begin_vertex>`,
          `#include <begin_vertex>
          
            ${compute}
            
            transformed = pos;
            
          `
        );
        //console.log(shader.vertexShader);
      }
    })
  }
}

let gu = {
  time: { value: 0 }
};

let scene = new THREE.Scene();
scene.background = new THREE.Color(0xff4444);

let camera = new THREE.PerspectiveCamera(30, innerWidth / innerHeight, 1, 1000);
camera.position.set(1, 1, 0.75).setLength(25);

let renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
renderer.setPixelRatio(devicePixelRatio);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
document.body.appendChild(renderer.domElement);

window.addEventListener("resize", (event) => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});

let controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.enablePan = false;
controls.maxPolarAngle = Math.PI / 3;

let camShift = 1;
controls.target.set(0, -camShift, 0);
camera.position.y -= camShift;

let light = new THREE.DirectionalLight(0xffffff, Math.PI * 1);
light.position.set(0, 4, 5);
light.castShadow = true;
let shadowCamSize = 6;
light.shadow.camera.left = -shadowCamSize;
light.shadow.camera.right = shadowCamSize;
light.shadow.camera.top = shadowCamSize;
light.shadow.camera.bottom = -shadowCamSize;
light.shadow.camera.near = 0.1;
light.shadow.camera.far = 50;
light.shadow.mapSize.width = 2048;
light.shadow.mapSize.height = 2048;
light.shadow.bias = -0.001;
//console.log(light.shadow.camera);
scene.add(light, new THREE.AmbientLight(0xffffff, Math.PI * 0.5));

// <true fun>

let floorBase = new FloorBase();
floorBase.receiveShadow = true;
scene.add(floorBase);

let stripes = new Ribbons(gu, 17);
stripes.castShadow = true;
stripes.receiveShadow = true;
scene.add(stripes);

// </true fun>

let clock = new THREE.Clock();
let t = 0;

renderer.setAnimationLoop(() => {
  let dt = clock.getDelta();
  t += dt;
  controls.update();
  floorBase.update(camera);
  gu.time.value = t;
  renderer.render(scene, camera);
});
