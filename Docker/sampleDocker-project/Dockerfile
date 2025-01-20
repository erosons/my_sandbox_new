# This is the 
FROM node:14

#Switch to the working directory specified
WORKDIR /app  

#Copy the file to the current working directory specified above
COPY package.json .

#This install the package before in current directory 
RUN npm install

#copy everything from the folder into the docker Current working dorectory(CWD)
COPY . ./

#using build-arguments which can then be passed at docker build time.
ARG name=defaultValue
ARG name

#using ENV variable in your Dockerfile

ENV PORT 3000

# this exposes the port for listening to traffic
EXPOSE ${PORT}

#excute this command on the terminal or command line
CMD [ "node", "app.mjs" ]