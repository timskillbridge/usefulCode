
<!-- NPM -->


Node Package Manager

Base Commands
npm -v Returns currently installed version
npm init
    Runs through several questions
        name (all lowercase)
        version
        description
        entry point (index.js)
        test command
        git repo if applicable
        keywords if applicable
        author
        license if applicable
    This generates a json object
        scripts section will execute commands using key value pairs. keys are the name to call, value is what is executed
        start, for example, will call index.js using "npm run start"
install axios using terminal "npm install axios"
    This will not install it to the system, but to the project by creating:
    A directory called node_modules
    A package-lock.json (don't touch it)
    A line in package.json called dependencies
Add a .gitignore (touch .gitignore)
    Add "node_modules" to the .gitignore file
Import statements:
    

