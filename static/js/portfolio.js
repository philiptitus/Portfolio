// Portfolio Timeline JavaScript

// Main initialization
document.addEventListener("DOMContentLoaded", () => {
    // Initialize components
    initForestBackground()
    initTimeline()
    initParticles()
  
    // Start animations
    animateElements()
  
    // Handle scroll events
    window.addEventListener("scroll", handleScroll)
    window.addEventListener("resize", handleResize)
  
    // Initial scroll check
    handleScroll()
  })
  
  // Forest background setup
  function initForestBackground() {
    const forestBackground = document.createElement("div")
    forestBackground.className = "forest-background"
  
    const parallaxTrees = document.createElement("div")
    parallaxTrees.className = "parallax-trees"
  
    const fogLayer = document.createElement("div")
    fogLayer.className = "fog-layer"
  
    const northernLights = document.createElement("div")
    northernLights.className = "northern-lights"
  
    forestBackground.appendChild(northernLights)
    forestBackground.appendChild(parallaxTrees)
    forestBackground.appendChild(fogLayer)
  
    document.body.appendChild(forestBackground)
  }
  
  // Timeline setup
  function initTimeline() {
    const timelineItems = document.querySelectorAll(".timeline-item")
    if (timelineItems.length === 0) return
  
    // Add tier classes to project cards
    timelineItems.forEach((item, index) => {
      // For demo purposes, assign S tier to first, A to second, and alternate B and A for rest
      let tierClass
      if (index === 0) {
        tierClass = "tier-s"
      } else if (index === 1) {
        tierClass = "tier-a"
      } else {
        tierClass = index % 2 === 0 ? "tier-b" : "tier-a"
      }
  
      item.classList.add(tierClass)
  
      // Add tier indicator
      const tierIndicator = document.createElement("div")
      tierIndicator.className = "tier-indicator"
      tierIndicator.textContent = tierClass.split("-")[1].toUpperCase()
      item.querySelector(".pCol").appendChild(tierIndicator)
    })
  }
  

  

  

  

  
  // Particle system initialization
  function initParticles() {
    const particlesContainer = document.createElement("div")
    particlesContainer.className = "particles-container"
    document.body.appendChild(particlesContainer)
  
    // Create leaves
    for (let i = 0; i < 20; i++) {
      createParticle("leaf", particlesContainer)
    }
  
    // Create fireflies
    for (let i = 0; i < 30; i++) {
      createParticle("firefly", particlesContainer)
    }
  }
  
  // Create individual particles
  function createParticle(type, container) {
    const particle = document.createElement("div")
    particle.className = `particle ${type}`
  
    // Random starting position
    const startX = Math.random() * window.innerWidth
    const startY = Math.random() * window.innerHeight
  
    particle.style.left = `${startX}px`
    particle.style.top = `${startY}px`
  
    // Random animation delay
    particle.style.animationDelay = `${Math.random() * 10}s`
  
    // For leaves, random rotation
    if (type === "leaf") {
      particle.style.transform = `rotate(${Math.random() * 360}deg)`
    }
  
    container.appendChild(particle)
  }
  
  // Handle scroll events
  function handleScroll() {
    const scrollPosition = window.scrollY
  
    // Animate timeline items on scroll
    const timelineItems = document.querySelectorAll(".timeline-item")
    timelineItems.forEach((item) => {
      const itemTop = item.offsetTop
      const itemHeight = item.offsetHeight
  
      if (scrollPosition + window.innerHeight * 0.8 > itemTop) {
        item.classList.add("visible")
      }
    })
  
    // Parallax effect for background
    const parallaxTrees = document.querySelector(".parallax-trees")
    if (parallaxTrees) {
      parallaxTrees.style.transform = `translateY(${scrollPosition * 0.1}px)`
    }
  
    const northernLights = document.querySelector(".northern-lights")
    if (northernLights) {
      northernLights.style.transform = `translateY(${scrollPosition * 0.05}px)`
    }
  }
  
  // Handle window resize
  function handleResize() {
    // Re-check scroll position after resize
    handleScroll()
  }
  
  // Animate elements
  function animateElements() {
    // Animate timeline line glow
    const timelineLine = document.querySelector(".timeline-line")
    if (timelineLine) {
      setInterval(() => {
        const glow = timelineLine.querySelector("::before") || timelineLine
        timelineLine.style.opacity = 0.8 + Math.random() * 0.2
      }, 2000)
    }
  
    // Animate fireflies
    setInterval(() => {
      const fireflies = document.querySelectorAll(".firefly")
      fireflies.forEach((firefly) => {
        firefly.style.opacity = Math.random() * 0.8
  
        // Random movement
        const xMove = (Math.random() - 0.5) * 50
        const yMove = (Math.random() - 0.5) * 50
  
        firefly.style.transform = `translate(${xMove}px, ${yMove}px)`
      })
    }, 3000)
  }
  