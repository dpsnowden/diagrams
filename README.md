
# Diagrams

 Catch all repo for experimenting with diagrams as code. D2, Mermaid, Structurizr, Python Diagrams etc.  It also serves as an inventory of diagrams describing various facets of IOOS/DMAC.  See [ioos.us](https://ioos.us/) [ioos.noaa.gov](https://ioos.noaa.gov/data/) and [ioos.github.io](https://ioos.github.io/).  Where is the data and where does it need to go?

## Tools

### Mermaid

- [mermaid](https://mermaid.js.org/) esp the VSCode and Obsidian plugins

### Python Diagrams

- [Python diagrams](https://diagrams.mingrammer.com/)

### C4 and Structurizr

- [C4](https://c4model.com/): a lightweight architecture model that is approachable for many different roles
- [Structurizr](https://docs.structurizr.com/): a software implementation using the C4 model to create and render diagrams.
- [sturcutrizr-lite](https://docs.structurizr.com/lite)


Steps:

- Install Docker command line and Docker Desktop
- Install [Structurizr Lite](https://docs.structurizr.com/lite/installation) docker container.

Running Structurizr Lite locally for the various models in development:

HFRNet is one project I was working on initially. Launching Structurizr Lite on the hfrnet DSL code folder

```zsh
docker run -it --rm -p 8080:8080 -v /Volumes/develop/hfrnet/architecture/:/usr/local/structurizr structurizr/lite
```

Currently, download all the diagrams from the web server in png and svg formats and put them in a Google Slide show, there has to be a better way.  Experiment with Github pages later

### D2

- [D2](https://d2lang.com/)

Links to references:

Directory structure that might make it easier to build models that share components (icons, model views, themes)
```zsh
/dev/d2
/dev/d2/icons
/dev/d2/hfr
/dev/d2/hfr/context
/dev/d2/hfr/container/
/dev/d2/hfr/component
/dev/d2/hfr/data-flow
```

### Jekyll, Github Pages, and Github Actions

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

## Topics

### Global Telecommunications System

[gts-workflow](./gts-workflow/)

GTS, the NOAA Telecomm Gateway, NDBC and all things operational within NOAA

### High Frequency Radar

[hfr](./hfr)

and [ioos/hfrnet](http://github.com/ioos/hfrnet)

### Unified Forecast System Coastal Application

[UFS-Coastal](./ufs-coastal/)

### Profiling Gliders

### IOOS DMAC

TODO: Populate this with existing drawio diagrams.  Can these be moved into a repo?  Just images or links to actual draw.io URLs?

## License

This project is licensed under the Creative Commons-0 License - see the LICENSE file for details

## References

Read this for an intro to Github Pages.  Great article [Least you need to know about Github pages](https://tomcam.github.io/least-github-pages/)