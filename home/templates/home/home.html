{% extends 'base.html' %}

{% block body %}
<div class="container">
    <div class="col-md-8">
        <h2>Home</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.post }}
            <br>
            <button type="submit">Submit</button>
        </form>
        <h2>{{ text }}</h2>
        {% for post in posts %}
            <h1>{{ post.post }}</h1>
            <p>Posted by {{ post.user.get_full_name }} on {{ post.created }}</p>
        {% endfor %}
    </div>
    <div class="col-md-4">
        <h2>Other People</h2>
        {% for user in users %}
            <a href="{% url 'accounts:view_profile_with_pk' pk=user.pk %}">
                <h3>{{ user.username }}</h3>
            </a>
            {% if not user in friends %}
            <a href="{% url 'home:change_friends' operation='add' pk=user.pk %}">
            <button type="button" class="btn btn-success">Add Friend</button>
            </a>
            {% endif %}
        {% endfor %}
        <h2>Friends</h2>
        {% for friend in friends %}
            <a href="{% url 'accounts:view_profile_with_pk' pk=friend.pk %}">
                <h3>{{ friend.username }}</h3>
            </a>
            <a href="{% url 'home:change_friends' operation='remove' pk=friend.pk %}">
            <button type="button" class="btn btn-default">Remove Friend</button>
            </a>
        {% endfor %}
    </div>
</div>
{% endblock %}
