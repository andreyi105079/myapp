{% for dev in data_dev %}
<font style="font-size: 10px;">{{ dev['number'] }}</font>
<font style="font-size: 10px;color: red;">{{ dev['name'] }}</font>
<font style="font-size: 10px;color: red;">{{ dev['price'] }}</font>
<font style="font-size: 10px;color: red;">{{ dev['finance'] }}</font>
<font style="font-size: 10px;color: red;">{{ dev['state'] }}</font> <br>
{% endfor %}
