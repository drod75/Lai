---
title: "Home Page"
layout: default
---

<div class="container mx-auto px-4">
  <div class="py-8">
    <h1 class="text-4xl font-bold text-center">{{ site.data.home.introduction.pitch }}</h1>
    <p class="mt-4 text-lg text-center">{{ site.data.home.introduction.description }}</p>
  </div>

  <div class="py-8">
    <h2 class="text-3xl font-bold">About the Creator</h2>
    <div class="mt-4">
      <p><span class="font-bold">Name:</span> {{ site.data.home.introduction.creator }}</p>
      <p><span class="font-bold">College:</span> {{ site.data.home.introduction.college }}</p>
      <p><span class="font-bold">Year:</span> {{ site.data.home.introduction.year }}</p>
      <p><span class="font-bold">Extracurricular Activities:</span> {{ site.data.home.introduction.extracurricular }}</p>
    </div>
  </div>

  {% for section_file in site.data.home %}
    {% assign section_name = section_file[0] %}
    {% if section_name != "introduction" %}
      <div class="py-8">
        <h2 class="text-3xl font-bold">{{ section_name | capitalize }}</h2>
        {% for item in section_file[1] %}
          <div class="mt-4">
            <h3 class="text-2xl font-bold">{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </div>
        {% endfor %}
      </div>
    {% endif %}
  {% endfor %}
</div>
