var population

var target;
var count = 0
//createa target vector and apply the position
target = createVector(width/2, 40)

//maximum util function
function findMax(items, predicate) {
  if (!predicate) {
    predicate = function(item) {
      return item
    }
  }
  
  //if there is predicate
  if (!items) {
    return null
  }
  
  var currentMax = items[0]
  for (var j = 1; j < items.length; j++) {
     if ( predicate(items[j]) >= predicate(currentMax)) {
       currentMax = items[j]
     }
  }
  return currentMax
}

function setup() {
	createCanvas(1000, 700)
  population = new Population(30)
  target = createVector(50, 200)
  //run 
 
 
  
}

function draw() {
	background(0)
  fill(123, 222, 122, 400)
  rect(this.target.x, this.target.y, 40, 20)
  count++
  if (count >= 600) {
    count = 0
    population.generateMatingPool()
    //i must be able to say
    //population.generateMatingPool()
    //population.reproduce()
    //population.evaluate()
  } else{
    population.run()  
  }
 	
  
  
}

function Population(n) {
	this.n = n
  this.particles = []
  for(var i = 0; i < this.n; i++ ) {
  	this.particles.push(new Particle()) 
    
   }
   
   this.run = function() {
   		for (var i = 0; i < this.particles.length; i++) {
      	this.particles[i].show()
				this.particles[i].update()
        
      }
   }
   
   this.generateMatingPool = function() {
      //first we calcalate the best fitness
     //and according to the fitness we createa mating poool
     //from the mating pool we select the two parents
     //from the two parents, we create a new child
     //apply the mutation
     var matingPool = []
     var bestParent = findMax(this.particles, function(particle) {
       return particle.fitness()
     })
     
     var maxFitness = bestParent.fitness()
     
     for (var i = 0; i < this.particles.length; i++) {
       //we have to take each particle , and cacluate the normalized fitenss
       var n = floor(this.particles[i].fitness() / maxFitness * 100)
       //push the parents in the mating pool for n time
       for (var j = 0; j < n; j++ ){
         matingPool.push(this.particles[i])
       }
     }
     
     //select two parentss from the mating pool
     //var parentA = random(matingPool)
     //var parentB = random(matingPool)
     //now do the cross over and generate new child
     var newParticles = []
     for (var k = 0; k < this.n; k++){
       var parentA = random(matingPool).dna
       var parentB = random(matingPool).dna
       var childDna = parentA.crossover(parentB)
       newParticles.push(new Particle(childDna))
     }
     this.particles = newParticles
     
     
     
     
     
     
   }
}

function Particle(dna) {
	this.position = createVector(width/2, height)
  this.velocity = createVector()
  this.acc = createVector()
  this.color = {
    r: random(255),
    g: random(255),
    b: random(255)
  }
  
  if (dna) {
    this.dna = dna
  } else {
    this.dna = new Dna()
   
  }
   
  //this.tilt = createVector(2, 2)
  
  this.show = function() {
  		push()
      fill(this.color.r, this.color.g, this.color.b, 400)
      noStroke()
      translate(this.position.x, this.position.y)
      rotate(this.velocity.heading())
      rectMode(CENTER)
  		rect(0, 0, 30,  10)
    //
      pop()
      
  }
  
  this.update = function() {
    //aply the dna force every frame, since this function is called every frame
   
    this.applyForce(this.dna.forces[count])
    
  	this.position.add(this.velocity)
    this.velocity.add(this.acc)
    this.acc.mult(0)
    this.velocity.limit(3)
        
  }
  
  this.applyForce = function(v) {
  	this.acc.add(v)
  }
  
  //algorithms for fiteness calcuation
  
  this.fitness = function() {
    var f = dist(this.position.x, this.position.y, target.x, target.y)
    return 1 / f; //les the distance then more the fitness
  }
  

}

function Dna(forces) {
  //its the pheno type of the algorithm
  //also know as the internal encoding
  if (forces) {
    this.forces = forces
  } else {
    this.forces = []
    for (var i = 0; i < 600; i++) {
      this.forces.push(p5.Vector.random2D())
    }
  }
  
  this.crossover = function(partner) {
    var newForces = []
    var randomMedian = floor(random(this.forces.length))
    for(var i = 0; i < this.forces.length; i++){
      if (i < randomMedian) {
        newForces[i] = this.forces[i]
      } else {
        newForces[i] = partner.forces[i]
      }
    }
    
    return new Dna(newForces);
   }
}
//