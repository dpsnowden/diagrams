
# Diagrams

 Catch all repo for experimenting with diagrams as code. D2, Mermaid, Structurizr, Python Diagrams etc.  It also serves as an inventory of diagrams describing various facets of IOOS/DMAC.  See [ioos.us](https://ioos.us/) [ioos.noaa.gov](https://ioos.noaa.gov/data/) and [ioos.github.io](https://ioos.github.io/).  Where is the data and where does it need to go?

## Tools

- This is helpful to make VSCode snippets and [templates](https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode)

### Mermaid

- [mermaid](https://mermaid.js.org/) esp the VSCode and Obsidian plugins

### Python Diagrams

- [Python diagrams](https://diagrams.mingrammer.com/)

### C4 and Structurizr

[C4 Cheatsheet](c4-structurizr/c4.md)

### D2

- [D2](d2/d2.md)

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

Most complete description of HFRNet is at [ioos/hfrnet](http://github.com/ioos/hfrnet)
[hfr-data-flow.d2](./hfr/hfr-data-flow.d2)
![hfr-data-flow.svg](./hfr/hfr-data-flow.svg)

### Unified Forecast System Coastal Application

[UFS-Coastal](./ufs-coastal/)

### Profiling Gliders

### IOOS DMAC

TODO: Populate this with existing drawio diagrams.  Can these be moved into a repo?  Just images or links to actual draw.io URLs?

## License

This project is licensed under the Creative Commons-0 License - see the LICENSE file for details

## References

Read this for an intro to Github Pages.  Great article [Least you need to know about Github pages](https://tomcam.github.io/least-github-pages/)