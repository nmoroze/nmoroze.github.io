---
layout: default
title: Projects
---

## Projects
{% for project in site.data.projects %}
{% include project.html project=project %}
{% endfor %}
