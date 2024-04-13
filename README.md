# diagrams
s
 Catch all repo for experimenting with diagrams as code. D2, Mermaid, Structurizr, Python Diagrams etc.

This project is an attempt to learn a few things and accomplish something useful at the same time.  My learning goals include:

- [C4](https://c4model.com/): a lightweight architecture model that is approachable for many different roles
- Structurizr: a software implementation using the C4 model to create and render diagrams.
- Diagrams as Code: Structurizr DSL, D2, Python Diagrams, and maybe mermaid.  Goal is to be able to embed the diagrams into the same Github repo that is used for project planning.
- Docker: Just enough to figure out how to deploy a web server and the Structurizr Lite web server
- Jekyll: to host and automatically build static site

The notes in this README are more notes to self than instructions for others to contribute.  

## Dependencies

- [D2](https://d2lang.com/)
- [mermaid](https://mermaid.js.org/) esp the VSCode and Obsidian plugins
- [sturcutrizr-lite](https://docs.structurizr.com/lite)
- [Python diagrams](https://diagrams.mingrammer.com/)

## Diagrams as Code

Initially, the diagrams were written using the C4 module in Python Diagrams.  This immediately sucked and I started looking at the Structurizr DSL as a better tool.  Structurizr is a much better tool to build the overall model of the System.  However, it's not a general diagramming tool.  For freeform diagrams, something like D2 is a little better.  Maintain the system model in Structurizr and fill in with Python Diagrams, D2 or Mermaid for one off visualizations.

### C4 and Structurizr

- [C4](https://c4model.com/): a lightweight architecture model that is approachable for many different roles
- [Structurizr](https://docs.structurizr.com/): a software implementation using the C4 model to create and render diagrams.

Steps:

- Install Docker command line and Docker Desktop
- Install [Structurizr Lite](https://docs.structurizr.com/lite/installation) docker container.

Running Structurizr Lite locally for the various models in development:

HFRNet is one project I was working on initially. Launching Structurizr Lite on the hfrnet DSL code folder

```zsh
docker run -it --rm -p 8080:8080 -v /Volumes/develop/hfrnet/architecture/:/usr/local/structurizr structurizr/lite
```

Currently, download all the diagrams from the web server in png and svg formats and put them in a Google Slide show, there has to be a better way.  Experiment with Github pages later

## D2

Also pretty cool and more extensible than C4.   Useful for things that don't fit the C4 model.

Links to references:

-

## Learning Jekyll and Github Pages

Basic site building on Github using Jekyll (locally first) and also figure out a basic git pull workflow for suggesting changes correctly.  Components include:

- [Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll) and running [Jekyll locally](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
- github-cli
- More skill with VSCode as a development environment
- Incorporating the C4 build process below into Github via actions
- Figuring out a better local development workflow for VSCode preiews of workspace.dsl
- Incorporating external markdown files into C4/Structurizr.
- Using D2 as a way to develop less structured C4 diagrams to supplement (or mermaid? There are at least 2 existing mermaid plugins for VSCode)

Build and serve the site from the local project directory ([from Jekyl quick start](https://jekyllrb.com/docs/):

```zsh
bundle exec jekyll serve
```

Software and Tools:

- [x] Download a test dsl model
- [x] Test migrating the models into dsl start with one file for everything
- [x] Research creating output files, including SVG
- [x] Utility script to create diagrams and copy files from ~/Downloads to site directory
- [ ] Research integrating Github and Github actions
- [ ] Research the structurizr-cli and see if it's easier to create output images with that.

## Getting Started

## License

This project is licensed under the Creative Commons-0 License - see the LICENSE file for details

## References

Read this for an intro to Github Pages.  Great article [Least you need to know about Github pages](https://tomcam.github.io/least-github-pages/)