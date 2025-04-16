// Forest Portfolio Timeline JavaScript

// Main initialization
document.addEventListener("DOMContentLoaded", () => {
    // Initialize components
    initForestBackground()
    initTreeTimeline()
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
  
  // Tree timeline setup
  function initTreeTimeline() {
    const portfolioContent = document.querySelector(".portfolioContentMain")
    if (!portfolioContent) return
  
    // Create tree timeline container
    const treeTimeline = document.createElement("div")
    treeTimeline.className = "tree-timeline"
  
    // Create tree trunk
    const treeTrunk = document.createElement("div")
    treeTrunk.className = "tree-trunk"
  
    // Add vines to the tree trunk
    addVinesToTree(treeTrunk)
  
    treeTimeline.appendChild(treeTrunk)
  
    // Wrap existing content
    portfolioContent.parentNode.insertBefore(treeTimeline, portfolioContent)
    treeTimeline.appendChild(portfolioContent)
  
    // Add tier classes to project cards
    const projectCards = document.querySelectorAll(".pColMain")
    if (projectCards.length === 0) {
      createEmptyState(treeTimeline)
      return
    }
  
    // Calculate total height needed for the timeline
    const totalHeight = projectCards.length * 300 + 200 // 300px per project + extra space
  
    // Set minimum height for the timeline container
    treeTimeline.style.minHeight = `${totalHeight}px`
  
    // Set height for the portfolio row to accommodate all projects
    const portfolioRow = document.querySelector(".portfolioRow")
    if (portfolioRow) {
      portfolioRow.style.height = `${totalHeight}px`
    }
  
    // Assign tiers to projects (for demo, assigning randomly)
    const tiers = ["tier-s", "tier-a", "tier-b"]
    projectCards.forEach((card, index) => {
      // For demo purposes, assign S tier to first, A to second, and alternate B and A for rest
      let tierClass
      if (index === 0) {
        tierClass = "tier-s"
      } else if (index === 1) {
        tierClass = "tier-a"
      } else {
        tierClass = index % 2 === 0 ? "tier-b" : "tier-a"
      }
  
      card.classList.add(tierClass)
  
      // Add tier indicator
      const tierIndicator = document.createElement("div")
      tierIndicator.className = "tier-indicator"
      tierIndicator.textContent = tierClass.split("-")[1].toUpperCase()
      card.querySelector(".pCol").appendChild(tierIndicator)
  
      // Position project cards alternating left and right
      positionProjectCard(card, index, totalHeight)
  
      // Create branches - one per project
      createBranch(card, index, tierClass)
    })
  }
  
  // Add vines to the tree trunk
  function addVinesToTree(treeTrunk) {
    // Create 4 vines
    for (let i = 1; i <= 4; i++) {
      const vine = document.createElement("div")
      vine.className = `vine vine-${i}`
  
      // Add leaves to each vine
      const leafCount = Math.floor(Math.random() * 4) + 3 // 3-6 leaves per vine
  
      for (let j = 0; j < leafCount; j++) {
        const leaf = document.createElement("div")
        leaf.className = "vine-leaf"
  
        // Position leaf along the vine
        const position = (j / leafCount) * 100
        leaf.style.top = `${position}%`
  
        // Alternate leaf sides
        if (j % 2 === 0) {
          leaf.style.left = "-8px"
          leaf.style.transform = "rotate(-45deg)"
        } else {
          leaf.style.right = "-8px"
          leaf.style.transform = "rotate(135deg)"
        }
  
        vine.appendChild(leaf)
      }
  
      treeTrunk.appendChild(vine)
    }
  }
  
  // Position project cards alternating left and right
  function positionProjectCard(projectCard, index, totalHeight) {
    const isEven = index % 2 === 0
    const verticalPosition = 150 + index * 300 // Space projects vertically
  
    projectCard.style.position = "absolute"
    projectCard.style.top = `${verticalPosition}px`
  
    if (isEven) {
      // Position on the right side of the tree
      projectCard.style.left = "55%"
    } else {
      // Position on the left side of the tree
      projectCard.style.left = "5%"
    }
  }
  
  // Create branches connecting to project cards
  function createBranch(projectCard, index, tierClass) {
    const branch = document.createElement("div")
    branch.className = `branch branch-${tierClass.split("-")[1]}`
    branch.setAttribute("data-index", index)
  
    // Position branch based on index (alternating left/right)
    const isEven = index % 2 === 0
    const verticalPosition = 150 + index * 300 + 100 // Align with the middle of the card
  
    branch.style.top = `${verticalPosition}px`
  
    if (isEven) {
      // Branch extends from tree to the right
      branch.style.left = "calc(50% + 20px)" // Start from right side of trunk
      branch.style.width = "150px"
      branch.style.transform = "translateY(-50%) rotate(-10deg)"
    } else {
      // Branch extends from tree to the left
      branch.style.left = "calc(50% - 170px)" // End at left side of trunk
      branch.style.width = "150px"
      branch.style.transform = "translateY(-50%) rotate(190deg)"
    }
  
    document.querySelector(".tree-timeline").appendChild(branch)
  }
  
  // Create empty state when no projects
  function createEmptyState(container) {
    const emptyState = document.createElement("div")
    emptyState.className = "empty-state"
  
    const emptyTree = document.createElement("div")
    emptyTree.className = "empty-tree"
  
    const emptyMessage = document.createElement("div")
    emptyMessage.className = "empty-message"
    emptyMessage.textContent = "No projects yet"
  
    const emptySubmessage = document.createElement("div")
    emptySubmessage.className = "empty-submessage"
    emptySubmessage.textContent = "The forest awaits your creations"
  
    emptyState.appendChild(emptyTree)
    emptyState.appendChild(emptyMessage)
    emptyState.appendChild(emptySubmessage)
  
    container.appendChild(emptyState)
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
  
    // Animate branches on scroll
    const branches = document.querySelectorAll(".branch")
    branches.forEach((branch) => {
      const index = Number.parseInt(branch.getAttribute("data-index"))
      const branchPosition = Number.parseInt(branch.style.top)
  
      if (scrollPosition + window.innerHeight * 0.8 > branchPosition) {
        branch.classList.add("branch-visible")
  
        // Also make the corresponding project card visible
        const projectCards = document.querySelectorAll(".pColMain")
        if (projectCards[index]) {
          projectCards[index].classList.add("visible")
        }
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
    // Check if we're on mobile
    const isMobile = window.innerWidth < 768
  
    if (isMobile) {
      // Adjust for mobile view
      const projectCards = document.querySelectorAll(".pColMain")
      projectCards.forEach((card, index) => {
        card.style.position = "relative"
        card.style.top = "0"
        card.style.left = "0"
      })
    } else {
      // Re-position for desktop
      const projectCards = document.querySelectorAll(".pColMain")
      const totalHeight = projectCards.length * 300 + 200
  
      projectCards.forEach((card, index) => {
        positionProjectCard(card, index, totalHeight)
      })
    }
  }
  
  // Animate elements
  function animateElements() {
    // Animate tree sap flow
    const treeTrunk = document.querySelector(".tree-trunk")
    if (treeTrunk) {
      setInterval(() => {
        const sapGlow = treeTrunk.querySelector(".sap-glow") || treeTrunk
        sapGlow.style.opacity = 0.3 + Math.random() * 0.3
      }, 2000)
    }
  
    // Animate vine leaves
    const vineLeaves = document.querySelectorAll(".vine-leaf")
    vineLeaves.forEach((leaf) => {
      // Random subtle movement
      setInterval(
        () => {
          const rotateAmount = Math.random() * 10 - 5 // -5 to +5 degrees
          leaf.style.transform = leaf.style.transform.replace(
            /rotate$$[^)]+$$/,
            `rotate(${Number.parseInt(leaf.style.transform.match(/rotate$$([^)]+)$$/)[1]) + rotateAmount}deg)`,
          )
        },
        3000 + Math.random() * 2000,
      )
    })
  
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
  