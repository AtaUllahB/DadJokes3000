<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--     <title>DadJoke 3000 with DALL·E</title> -->
</head>
<body>

<h1>DadJoke 3000 with DALL·E</h1>


<img src="https://github.com/AtaUllahB/Theatre/blob/master/screenshots/login.png](https://github.com/AtaUllahB/DadJokes3000/blob/c7a382e20afdcf57a16b3b8eb32f6685d099338b/demo.gif?raw=true">


<p>This is a simple joke generation application using <strong>Tkinter</strong>, <strong>OpenAI GPT</strong>, and <strong>DALL·E</strong> to generate funny dad jokes and create images based on the jokes.</p>

<h2>Features</h2>
<ul>
    <li><strong>Dad Jokes Generator</strong>: Enter a topic, and the app generates a dad joke using OpenAI GPT.</li>
    <li><strong>Image Generation</strong>: The app also generates an illustration of the dad joke using the DALL·E API.</li>
    <li><strong>Simple UI</strong>: The app has a clean user interface built with Tkinter.</li>
    <li><strong>Clear Button</strong>: You can clear the input and reset the display with a single click.</li>
</ul>

<h2>How to Run</h2>
<ol>
    <li>Clone the repository:
    
cd dadjoke3000
        </code></pre>
    </li>
    <li>Install the required dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Ensure you have a placeholder image in the root directory named <code>placeholder_image.png</code> (or update the code with your image path).</li>
    <li>Replace the OpenAI API key in the code:
        <pre><code>client = OpenAI(api_key='your-api-key')</code></pre>
    </li>
    <li>Run the app:
        <pre><code>python app.py</code></pre>
    </li>
</ol>

<h2>Dependencies</h2>
<ul>
    <li><strong>Tkinter</strong>: Provides the GUI framework.</li>
    <li><strong>OpenAI</strong>: Communicates with GPT and DALL·E for generating jokes and images.</li>
    <li><strong>Pillow</strong>: Handles image processing and display.</li>
    <li><strong>Requests</strong>: Fetches the generated image from DALL·E's API.</li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Enter a joke subject (e.g., "bananas").</li>
    <li>Click "Get my dad joke!" to generate a joke and an image.</li>
    <li>Use the "Clear" button to reset the input and display.</li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
