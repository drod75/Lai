---
title: "Home Page"
layout: default
---

<div class="container mx-auto px-4">

    <!-- introduction section -->
    <div class="card bg-blue-100 p-6 rounded-lg shadow-md my-8">
        <div class="py-4">
            <h1 class="text-4xl font-bold text-center text-blue-900">{{ site.data.home.introduction.pitch }}</h1>
            <p class="mt-4 text-lg text-center text-blue-800">{{ site.data.home.introduction.description }}</p>
        </div>
        
        <div class="py-4 mt-6 border-t border-blue-200">
            <h2 class="text-3xl font-bold mb-4 text-blue-900">About the Creator</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <p><span class="font-extrabold text-lg text-blue-900">Name:</span> {{ site.data.home.introduction.creator }}</p>
                <p><span class="font-extrabold text-lg text-blue-900">College:</span> {{ site.data.home.introduction.college }}</p>
                <p><span class="font-extrabold text-lg text-blue-900">Year:</span> {{ site.data.home.introduction.year }}</p>
                <p><span class="font-extrabold text-lg text-blue-900">Extracurricular Activities:</span> {{ site.data.home.introduction.extracurricular }}</p>
            </div>
        </div>
    </div>

    <!-- quick details section -->
    <div class="py-8">
        <h2 class="text-3xl font-bold border-b-2 border-blue-500 pb-2 mb-6 text-blue-900">
            {{ site.data.home.sections.title }}
        </h2>
        
        <div class="grid grid-cols-1 gap-6">
            {% for item in site.data.home.sections.items %}
                <div class="p-5 bg-white rounded-lg shadow-sm border-l-4 border-blue-600">
                    <h3 class="text-2xl font-bold text-blue-900">{{ item.title }}</h3>
                    <p class="text-gray-700 mt-2">{{ item.description }}</p>

                    <!-- tech stack sub section -->
                    {% if item.title == "Technologies Used" and item.categories %}
                        <div class="mt-6 space-y-4">
                            {% for category in item.categories %}
                                <div>
                                    <span class="text-sm font-bold uppercase tracking-wider text-blue-600">{{ category.name }}</span>
                                    <div class="flex flex-wrap gap-2 mt-2">
                                        {% for tech in category.techs %}
                                            <img src="{{ tech.shield }}" alt="{{ tech.name }}">
                                        {% endfor %}
                                    </div>
                                </div>
                            {% endfor %}
                        </div>
                    {% endif %}
                </div>
            {% endfor %}
                <div class="p-5 bg-white rounded-lg shadow-sm border-l-4 border-blue-600">
                    <h3 class="text-2xl font-bold text-blue-900">{{ site.data.home.timeline.title }}</h3>
                    <p class="text-gray-700 mt-2">{{ site.data.home.timeline.description }}</p>
                    <div class="mt-6">
                        <img src="{{ site.data.home.timeline.image }}" alt="timeline" >
                    </div>
                </div>
        </div>
    </div>


    <!-- pages -->
    <div class="py-8">
        <h2 class="text-3xl font-bold border-b-2 border-fuchsia-500 pb-2 mb-6 text-fuchsia-900">
            {{ site.data.home.pages.title }}
        </h2>
        
        <div class="grid grid-cols-1 gap-6">
            {% for item in site.data.home.pages.items %}
                <div class="p-5 bg-white rounded-lg shadow-sm border-l-4 border-fuchsia-600">
                    <h3 class="text-2xl font-bold text-fuchsia-900">{{ item.title }}</h3>
                    <p class="text-gray-700 mt-2">{{ item.description }}</p>
                </div>
            {% endfor %}
        </div>
    </div>



</div>