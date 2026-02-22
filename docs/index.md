---
title: "Home Page"
layout: default
---

<div class="container mx-auto px-4">
    <div class="card bg-green-100 p-6 rounded-lg shadow-md my-8">
        <div class="py-4">
            <h1 class="text-4xl font-bold text-center">{{ site.data.home.introduction.pitch }}</h1>
            <p class="mt-4 text-lg text-center">{{ site.data.home.introduction.description }}</p>
        </div>
        
        <div class="py-4 mt-6 border-t border-green-200">
            <h2 class="text-3xl font-bold mb-4">About the Creator</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <p><span class="font-extrabold text-lg">Name:</span> {{ site.data.home.introduction.creator }}</p>
                <p><span class="font-extrabold text-lg">College:</span> {{ site.data.home.introduction.college }}</p>
                <p><span class="font-extrabold text-lg">Year:</span> {{ site.data.home.introduction.year }}</p>
                <p><span class="font-extrabold text-lg">Extracurricular Activities:</span> {{ site.data.home.introduction.extracurricular }}</p>
            </div>
        </div>
    </div>

    {% for section_file in site.data.home %}
        {% assign section_name = section_file[0] %}
        {% assign section_data = section_file[1] %}
        
        {% if section_name != "introduction" %}
            <div class="py-8">
                <h2 class="text-3xl font-bold border-b-2 border-green-500 pb-2 mb-6">
                    {{ section_data.title }}
                </h2>
                
                <div class="grid grid-cols-1 gap-6">
                    {% for item in section_data.items %}
                        <div class="p-5 bg-white rounded-lg shadow-sm border-l-4 border-green-600">
                            <h3 class="text-2xl font-bold text-green-900">{{ item.title }}</h3>
                            <p class="text-gray-700 mt-2">{{ item.description }}</p>
                        </div>
                    {% endfor %}
                </div>
            </div>
        {% endif %}
    {% endfor %}
</div>