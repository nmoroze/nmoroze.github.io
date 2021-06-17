---
layout: default
title: Home
---

Hi! My name is Noah, and I'm currently a software engineer at [Zero
ASIC](https://zeroasic.com).

Prior to Zero ASIC I was a student at MIT, where I earned my BS and MEng in
electrical engineering and computer science. My [masters
thesis](https://pdos.csail.mit.edu/papers/moroze-meng.pdf) project
[Kronos](https://github.com/nmoroze/kronos) involved using formal verification
to prove a security property for an open-source processor. I worked on this
thesis with the Parallel and Distributed Operating Systems Group
[(PDOS)](https://pdos.csail.mit.edu/) in MIT CSAIL.

I'm passionate about making things, and I enjoy projects that involve the
intersection of hardware and software. Lately, I've taken a particular interest
in open-source digital hardware, tools for simplifying digital hardware design,
and using dedicated hardware for achieving new goals in performance or security.

If you're interested in the sort of stuff I'm working on, please consider
following me on [Twitter](https://twitter.com/NoahMoroze), where I post
occasional project updates, or [Github](https://github.com/nmoroze), where you
can find my open-source work!

<!-- Previously, I've worked on LIDAR firmware at [Waymo](https://waymo.com/),
and before that I worked on systems software at
[NVIDIA](https://www.nvidia.com/en-us/). -->

<!-- In my spare time, I sometimes build small combat robots at -->
<!-- [MITERS](http://miters.mit.edu/). I also used to help organize -->
<!-- [HackMIT](https://hackmit.org). -->

## [Featured Projects](#projects)
{% for project in site.data.projects %}
{% if project.featured %}
{% include project.html project=project %}
{% endif %}
{% endfor %}
