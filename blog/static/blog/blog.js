class Greeter {
  constructor (name) {
    this.name = name
  }

  getGreeting () {
    if (this.name === undefined) {
      return 'Hello, no name'
    }

    return 'Hello, ' + this.name
  }

  showGreeting (greetingMessage) {
    console.log(greetingMessage)
  }

  greet () {
    this.showGreeting(this.getGreeting())
  }
}

class DelayedGreeter extends Greeter {
  delay = 1000

  constructor (name, delay) {
    super(name)
    if (delay !== undefined) {
      this.delay = delay
    }
  }
  
  greet () {
    setTimeout(
      () => {
        this.showGreeting(this.getGreeting())
      }, this.delay
    )
  }
  
  greet2(){
    setTimeout(
      function() {
        this.showGreeting(this.getGreeting())
      }, this.delay
    ) 
  }  

  getGreeting2(){ 
    return 'aus'
  }
 }

function getGreeting(){ 
  console.info('greeting')
}

 function showGreeting(){ 
  console.info('show')
}

const g = new Greeter('Patchy')
g.greet()
const g2 = new DelayedGreeter('son')
g2.greet()