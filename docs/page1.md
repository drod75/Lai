---
layout: default
title: "Source docs Page"
---

<!-- agent folder -->
<div class="py-8">
    <h2 class="text-3xl font-bold border-b-2 border-blue-500 pb-2 mb-6 text-blue-900">
        {{ site.data.source.agent.title }}
    </h2>
    
    <div class="grid grid-cols-1 gap-6">
        {% for item in site.data.source.agent.items %}
            <div class="p-5 bg-white rounded-lg shadow-sm border-l-4 border-blue-600">
                <h3 class="text-2xl font-bold text-blue-900">{{ item.title }}</h3>
                <p class="text-gray-700 mt-2">{{ item.description }}</p>

                <!-- code block if -->
                {% if item.title == "Code Block"% and item.lines %}
                    <div class="mockup-code w-full">
                        {% for line in item.lines %}
                            <pre data-prefix="{{ forloop.index }}"><code>{{ line }}</code></pre>
                        {% endfor %}
                    </div>
                {% endif %}
            </div>
        {% endfor %}
    </div>
</div>


<!-- ui folder -->
<div class="py-8">
    <h2 class="text-3xl font-bold border-b-2 border-fuchsia-500 pb-2 mb-6 text-fuchsia-900">
        {{ site.data.source.ui.title }}
    </h2>
    
    <div class="grid grid-cols-1 gap-6">
        {% for item in site.data.source.ui.items %}
            <div class="p-5 bg-white rounded-lg shadow-sm border-l-4 border-fuchsia-600">
                <h3 class="text-2xl font-bold text-fuchsia-900">{{ item.title }}</h3>
                <p class="text-gray-700 mt-2">{{ item.description }}</p>

                <!-- code block if -->
                {% if item.title == "Code Block"% and item.lines %}
                    <div class="mockup-code w-full">
                        {% for line in item.lines %}
                            <pre data-prefix="{{ forloop.index }}"><code>{{ line }}</code></pre>
                        {% endfor %}
                    </div>
                {% endif %}
            </div>
        {% endfor %}
    </div>
</div>

<!-- utils folder -->
<div class="py-8">
    <h2 class="text-3xl font-bold border-b-2 border-purple-500 pb-2 mb-6 text-purple-900">
        {{ site.data.source.utils.title }}
    </h2>
    
    <div class="grid grid-cols-1 gap-6">
        {% for item in site.data.source.utils.items %}
            <div class="p-5 bg-white rounded-lg shadow-sm border-l-4 border-purple-600">
                <h3 class="text-2xl font-bold text-purple-900">{{ item.title }}</h3>
                <p class="text-gray-700 mt-2">{{ item.description }}</p>
            </div>
        {% endfor %}
    </div>
</div>
