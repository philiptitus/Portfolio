// ML Models - Interactive Elements
// ------------------------------------------------

// Wait for DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Initialize neural network background
    initNeuralBackground()
  
    // Initialize particles
    initParticles()
  
    // Initialize timeline (only on list page)
    if (document.querySelector(".timeline-container")) {
      initTimeline()
    }
  
    // Initialize animations for detail page
    if (document.querySelector(".ml-detail-container")) {
      initDetailAnimations()
    }
  
    // Initialize neural pathways for detail page
    if (document.querySelector(".ml-detail-container")) {
      initNeuralPathways()
    }
  })
  
  // Neural Network Background
  // ------------------------------------------------
  function initNeuralBackground() {
    const neuralBg = document.querySelector(".neural-bg")
    if (!neuralBg) return
  
    // Create SVG element
    const svgNS = "http://www.w3.org/2000/svg"
    const svg = document.createElementNS(svgNS, "svg")
    svg.setAttribute("width", "100%")
    svg.setAttribute("height", "100%")
    neuralBg.appendChild(svg)
  
    // Generate random nodes
    const nodeCount = Math.min(window.innerWidth / 8, 150) // Increased node count
    const nodes = []
  
    for (let i = 0; i < nodeCount; i++) {
      const x = Math.random() * window.innerWidth
      const y = Math.random() * window.innerHeight
      const radius = Math.random() * 3 + 1.5 // Larger nodes
  
      const node = document.createElementNS(svgNS, "circle")
      node.setAttribute("cx", x)
      node.setAttribute("cy", y)
      node.setAttribute("r", radius)
      node.setAttribute("fill", "rgba(255, 255, 255, 0.7)") // Brighter nodes
      node.setAttribute("data-active", "false")
      node.setAttribute("data-connections", "")
  
      svg.appendChild(node)
      nodes.push({
        element: node,
        x,
        y,
        radius,
        connections: [],
        active: false,
        activationTime: 0,
      })
    }
  
    // Generate connections between nodes
    for (let i = 0; i < nodes.length; i++) {
      const connections = Math.floor(Math.random() * 4) + 2 // More connections
  
      for (let j = 0; j < connections; j++) {
        const targetIndex = Math.floor(Math.random() * nodes.length)
        if (targetIndex !== i && targetIndex < nodes.length) {
          const line = document.createElementNS(svgNS, "line")
          line.setAttribute("x1", nodes[i].x)
          line.setAttribute("y1", nodes[i].y)
          line.setAttribute("x2", nodes[targetIndex].x)
          line.setAttribute("y2", nodes[targetIndex].y)
          line.setAttribute("stroke", "rgba(74, 136, 255, 0.3)") // Brighter connections
          line.setAttribute("stroke-width", "0.8") // Thicker lines
          line.setAttribute("data-active", "false")
  
          svg.appendChild(line)
  
          // Store connection references
          nodes[i].connections.push({
            target: targetIndex,
            element: line,
          })
  
          // Store connection indices as data attribute
          const currentConnections = nodes[i].element.getAttribute("data-connections")
          nodes[i].element.setAttribute(
            "data-connections",
            currentConnections ? `${currentConnections},${targetIndex}` : targetIndex,
          )
        }
      }
    }
  
    // Animate neural network
    function animateNeuralNetwork() {
      // Randomly activate nodes
      if (Math.random() < 0.05) {
        const randomNodeIndex = Math.floor(Math.random() * nodes.length)
        activateNode(randomNodeIndex)
      }
  
      // Update node states
      const currentTime = Date.now()
      nodes.forEach((node, index) => {
        if (node.active) {
          // Make node glow brighter
          node.element.setAttribute("fill", "rgba(255, 255, 255, 1)")
          node.element.setAttribute("r", node.radius * 1.5)
          node.element.setAttribute("filter", "drop-shadow(0 0 5px rgba(255, 255, 255, 0.8))")
  
          // Transmit signal to connected nodes after a delay
          if (currentTime - node.activationTime > 300) {
            transmitSignal(index)
            node.active = false
  
            // Gradually dim the node
            setTimeout(() => {
              node.element.setAttribute("fill", "rgba(255, 255, 255, 0.7)")
              node.element.setAttribute("r", node.radius)
              node.element.setAttribute("filter", "none")
            }, 300)
          }
        }
      })
  
      requestAnimationFrame(animateNeuralNetwork)
    }
  
    // Activate a node and prepare for signal transmission
    function activateNode(nodeIndex) {
      if (nodeIndex >= 0 && nodeIndex < nodes.length) {
        nodes[nodeIndex].active = true
        nodes[nodeIndex].activationTime = Date.now()
      }
    }
  
    // Transmit signal to connected nodes
    function transmitSignal(nodeIndex) {
      if (nodeIndex >= 0 && nodeIndex < nodes.length) {
        const node = nodes[nodeIndex]
  
        // Animate connections and activate target nodes
        node.connections.forEach((connection) => {
          // Animate the connection line
          const line = connection.element
          line.setAttribute("stroke", "rgba(74, 136, 255, 0.8)")
          line.setAttribute("stroke-width", "1.5")
  
          // Create signal animation along the line
          const signal = document.createElementNS(svgNS, "circle")
          signal.setAttribute("r", "2")
          signal.setAttribute("fill", "rgba(255, 255, 255, 0.9)")
          signal.setAttribute("filter", "drop-shadow(0 0 3px rgba(255, 255, 255, 0.8))")
          svg.appendChild(signal)
  
          // Animate signal along the path
          const startX = node.x
          const startY = node.y
          const endX = nodes[connection.target].x
          const endY = nodes[connection.target].y
  
          const startTime = Date.now()
          const duration = 500 // ms
  
          function animateSignal() {
            const elapsed = Date.now() - startTime
            const progress = Math.min(elapsed / duration, 1)
  
            const x = startX + (endX - startX) * progress
            const y = startY + (endY - startY) * progress
  
            signal.setAttribute("cx", x)
            signal.setAttribute("cy", y)
  
            if (progress < 1) {
              requestAnimationFrame(animateSignal)
            } else {
              // Remove signal and reset connection
              svg.removeChild(signal)
              setTimeout(() => {
                line.setAttribute("stroke", "rgba(74, 136, 255, 0.3)")
                line.setAttribute("stroke-width", "0.8")
              }, 200)
  
              // Activate target node
              activateNode(connection.target)
            }
          }
  
          animateSignal()
        })
      }
    }
  
    // Start the animation
    animateNeuralNetwork()
  }
  
  // Particles Background
  // ------------------------------------------------
  function initParticles() {
    const particlesContainer = document.querySelector(".particles-container")
    if (!particlesContainer) return
  
    // Create canvas element
    const canvas = document.createElement("canvas")
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
    particlesContainer.appendChild(canvas)
  
    const ctx = canvas.getContext("2d")
  
    // Generate particles
    const particleCount = Math.min(window.innerWidth / 15, 80) // Increased particle count
    const particles = []
  
    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 2.5 + 0.5, // Larger particles
        color: `rgba(${Math.floor(Math.random() * 100 + 155)}, ${Math.floor(Math.random() * 100 + 155)}, 255, ${Math.random() * 0.6 + 0.3})`, // Brighter particles
        speedX: Math.random() * 0.6 - 0.3,
        speedY: Math.random() * 0.6 - 0.3,
        connections: [],
      })
    }
  
    // Create connections between nearby particles
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x
        const dy = particles[i].y - particles[j].y
        const distance = Math.sqrt(dx * dx + dy * dy)
  
        if (distance < 150) {
          // Connection distance threshold
          particles[i].connections.push(j)
          particles[j].connections.push(i)
        }
      }
    }
  
    // Animation loop
    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height)
  
      // Draw connections
      particles.forEach((particle, i) => {
        particle.connections.forEach((j) => {
          const target = particles[j]
          const dx = particle.x - target.x
          const dy = particle.y - target.y
          const distance = Math.sqrt(dx * dx + dy * dy)
  
          if (distance < 150) {
            // Only draw if still in range
            ctx.beginPath()
            ctx.strokeStyle = `rgba(74, 136, 255, ${0.3 * (1 - distance / 150)})`
            ctx.lineWidth = 0.5
            ctx.moveTo(particle.x, particle.y)
            ctx.lineTo(target.x, target.y)
            ctx.stroke()
          }
        })
      })
  
      particles.forEach((particle) => {
        // Update position
        particle.x += particle.speedX
        particle.y += particle.speedY
  
        // Boundary check
        if (particle.x < 0 || particle.x > canvas.width) particle.speedX *= -1
        if (particle.y < 0 || particle.y > canvas.height) particle.speedY *= -1
  
        // Draw particle
        ctx.beginPath()
        ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2)
        ctx.fillStyle = particle.color
        ctx.fill()
  
        // Add glow effect
        ctx.beginPath()
        ctx.arc(particle.x, particle.y, particle.radius * 2, 0, Math.PI * 2)
        const gradient = ctx.createRadialGradient(
          particle.x,
          particle.y,
          particle.radius * 0.5,
          particle.x,
          particle.y,
          particle.radius * 2,
        )
        gradient.addColorStop(0, particle.color.replace(")", ", 0.3)").replace("rgba", "rgba"))
        gradient.addColorStop(1, particle.color.replace(")", ", 0)").replace("rgba", "rgba"))
        ctx.fillStyle = gradient
        ctx.fill()
      })
  
      requestAnimationFrame(animate)
    }
  
    animate()
  
    // Handle window resize
    window.addEventListener("resize", () => {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
    })
  
    // React to scroll
    window.addEventListener("scroll", () => {
      const scrollY = window.scrollY
      particles.forEach((particle) => {
        particle.y += scrollY * 0.01 * (Math.random() - 0.5)
  
        // Keep particles in bounds
        if (particle.y < 0) particle.y = canvas.height
        if (particle.y > canvas.height) particle.y = 0
      })
    })
  }
  
  // Timeline Navigation
  // ------------------------------------------------
  function initTimeline() {
    const timelineContainer = document.querySelector(".timeline-container")
    const timeline = document.querySelector(".timeline")
    const modelSections = document.querySelectorAll(".ml-model-section")
    const cards = document.querySelectorAll(".ml-card")
  
    if (!timeline || !modelSections.length) return
  
    // Create timeline marker
    const marker = document.createElement("div")
    marker.className = "timeline-marker"
    timeline.appendChild(marker)
  
    // Set timeline height
    timeline.style.height = `${document.body.scrollHeight - 80}px` // Account for header
  
    // Update marker position on scroll
    window.addEventListener("scroll", updateTimelineMarker)
  
    // Enable smooth scrolling
    enableSmoothScrolling()
  
    // Initial update
    updateTimelineMarker()
  
    function updateTimelineMarker() {
      const scrollPosition = window.scrollY
      const documentHeight = document.body.scrollHeight - window.innerHeight
  
      // Calculate marker position
      let markerPosition = (scrollPosition / documentHeight) * (timeline.offsetHeight - marker.offsetHeight)
  
      // Constrain marker within timeline
      markerPosition = Math.max(0, Math.min(markerPosition, timeline.offsetHeight - marker.offsetHeight))
  
      // Update marker position with smooth animation
      marker.style.transition = "top 0.3s ease-out"
      marker.style.top = `${markerPosition}px`
  
      // Update active section
      updateActiveSection(scrollPosition)
    }
  
    function updateActiveSection(scrollPosition) {
      let activeIndex = -1
      const viewportMiddle = scrollPosition + window.innerHeight / 2
  
      // Find the section that should be active based on scroll position
      modelSections.forEach((section, index) => {
        const sectionTop = section.offsetTop
        const sectionHeight = section.offsetHeight
  
        if (viewportMiddle >= sectionTop && viewportMiddle <= sectionTop + sectionHeight) {
          activeIndex = index
        }
      })
  
      // Update section and card states
      modelSections.forEach((section, index) => {
        if (index === activeIndex) {
          section.classList.remove("inactive")
          marker.classList.add("active")
  
          // Find the card in this section and activate it
          const card = section.querySelector(".ml-card")
          if (card) {
            card.classList.add("active")
          }
        } else {
          section.classList.add("inactive")
  
          // Find the card in this section and deactivate it
          const card = section.querySelector(".ml-card")
          if (card) {
            card.classList.remove("active")
          }
        }
  
        if (activeIndex === -1) {
          marker.classList.remove("active")
        }
      })
    }
  
    function enableSmoothScrolling() {
      // Add smooth scrolling to timeline marker clicks
      marker.addEventListener("click", () => {
        const scrollPosition = window.scrollY
        const documentHeight = document.body.scrollHeight - window.innerHeight
        const markerPosition = Number.parseFloat(marker.style.top || "0")
        const timelineHeight = timeline.offsetHeight - marker.offsetHeight
  
        const targetScrollPosition = (markerPosition / timelineHeight) * documentHeight
  
        window.scrollTo({
          top: targetScrollPosition,
          behavior: "smooth",
        })
      })
    }
  }
  
  // Detail Page Animations
  // ------------------------------------------------
  function initDetailAnimations() {
    const detailElements = document.querySelectorAll(
      ".ml-detail-header, .ml-detail-image, .ml-detail-content, .ml-related-card",
    )
  
    // Add fade-in animation to elements
    detailElements.forEach((element, index) => {
      element.style.opacity = "0"
      element.style.animationDelay = `${index * 0.2}s`
      element.classList.add("fade-in")
    })
  
    // Add pulse animation to badges
    const badges = document.querySelectorAll(".ml-badge")
    badges.forEach((badge) => {
      badge.classList.add("pulse")
    })
  }
  
  // Neural Pathways for Detail Page
  // ------------------------------------------------
  function initNeuralPathways() {
    const contentSections = document.querySelectorAll(".ml-detail-content, .ml-related-card")
    if (contentSections.length < 2) return
  
    // Create container for neural pathways
    const pathwaysContainer = document.createElement("div")
    pathwaysContainer.className = "neural-pathways-container"
    pathwaysContainer.style.position = "absolute"
    pathwaysContainer.style.top = "0"
    pathwaysContainer.style.left = "0"
    pathwaysContainer.style.width = "100%"
    pathwaysContainer.style.height = "100%"
    pathwaysContainer.style.pointerEvents = "none"
    pathwaysContainer.style.zIndex = "0"
    document.querySelector(".ml-detail-container").appendChild(pathwaysContainer)
  
    // Connect sections with neural pathways
    for (let i = 0; i < contentSections.length; i++) {
      for (let j = i + 1; j < contentSections.length; j++) {
        if (Math.random() < 0.7) {
          // 70% chance to create a connection
          createNeuralPathway(contentSections[i], contentSections[j], pathwaysContainer)
        }
      }
    }
  
    function createNeuralPathway(elementA, elementB, container) {
      const rectA = elementA.getBoundingClientRect()
      const rectB = elementB.getBoundingClientRect()
  
      // Calculate start and end points
      const startX = rectA.left + rectA.width / 2
      const startY = rectA.top + rectA.height / 2
      const endX = rectB.left + rectB.width / 2
      const endY = rectB.top + rectB.height / 2
  
      // Calculate distance and angle
      const dx = endX - startX
      const dy = endY - startY
      const distance = Math.sqrt(dx * dx + dy * dy)
      const angle = (Math.atan2(dy, dx) * 180) / Math.PI
  
      // Create pathway element
      const pathway = document.createElement("div")
      pathway.className = "neural-pathway"
      pathway.style.position = "absolute"
      pathway.style.width = `${distance}px`
      pathway.style.left = `${startX}px`
      pathway.style.top = `${startY}px`
      pathway.style.transform = `rotate(${angle}deg)`
  
      // Add to container
      container.appendChild(pathway)
  
      // Animate signal transmission
      setInterval(
        () => {
          const signal = document.createElement("div")
          signal.style.position = "absolute"
          signal.style.width = "8px"
          signal.style.height = "8px"
          signal.style.borderRadius = "50%"
          signal.style.backgroundColor = "rgba(74, 136, 255, 0.8)"
          signal.style.boxShadow = "0 0 10px rgba(74, 136, 255, 0.8)"
          signal.style.left = "0"
          signal.style.top = "-3px" // Center vertically
          signal.style.transition = "left 2s ease-out"
  
          pathway.appendChild(signal)
  
          // Start animation after a small delay
          setTimeout(() => {
            signal.style.left = `${distance}px`
          }, 10)
  
          // Remove signal after animation completes
          setTimeout(() => {
            pathway.removeChild(signal)
          }, 2100)
        },
        3000 + Math.random() * 2000,
      ) // Random interval between signals
    }
  
    // Update pathway positions on window resize
    window.addEventListener("resize", () => {
      // Remove existing pathways
      while (pathwaysContainer.firstChild) {
        pathwaysContainer.removeChild(pathwaysContainer.firstChild)
      }
  
      // Recreate pathways
      for (let i = 0; i < contentSections.length; i++) {
        for (let j = i + 1; j < contentSections.length; j++) {
          if (Math.random() < 0.7) {
            createNeuralPathway(contentSections[i], contentSections[j], pathwaysContainer)
          }
        }
      }
    })
  }
  