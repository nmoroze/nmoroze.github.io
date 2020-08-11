---
layout: default
title: Home
---

## [About](#about)
Hi! My name is Noah, and I'm an MEng student studying electrical engineering and
computer science at MIT. I'm passionate about making things, and I particularly
enjoy projects that involve the intersection of hardware and software (such as
embedded systems and robotics).

I'm currently working on my thesis in the Parallel and Distributed Operating
Systems Group [(PDOS)](https://pdos.csail.mit.edu/). My research revolves around
verifying security properties of computer processors.

Last summer I worked on LIDAR firmware at [Waymo](https://waymo.com/), and the
summer before that I worked on systems software at
[NVIDIA](https://www.nvidia.com/en-us/).

In my spare time, I sometimes build small combat robots at
[MITERS](http://miters.mit.edu/). I also used to help organize
[HackMIT](https://hackmit.org).

## [Projects](#projects)
{% for project in site.data.projects %}
{% include project.html project=project %}
{% endfor %}
