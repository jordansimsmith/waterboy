# Water Boy
A Raspberry Pi script that sends notifications when a plant needs watering.

![waterboy](https://user-images.githubusercontent.com/18223858/64070863-ea684580-ccc0-11e9-8bea-b66fb47e3b19.png)

## Usage
This project requires a Raspberry Pi to be setup with an external soil moisture detector. 
A .env file needs to be created in the `rpi` folder, follow .env.example for details.
Once configured, run the following commands to build and deploy the script.

- `make build` is used to download dependencies and package the project up for deployment.
- `make deploy` is used to deploy the build artifact to the Pi, using rsync over ssh.
