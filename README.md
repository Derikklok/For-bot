# Some Bot

This is a simple HTML page that embeds a chatbot .

## Structure

The HTML file is structured as follows:

- **DOCTYPE**: The document type declaration specifies that the file is an HTML5 document.
- **HTML**: The root element containing the entire content of the page.
- **Head**:
  - **Charset**: Specifies the character encoding as UTF-8.
  - **Viewport**: Ensures proper scaling on different devices.
  - **Title**: The title of the document, currently set to "Document".
- **Body**:
  - **Div**: Contains a header (`<h1>`) element with the text "some bot".
  - **Footer**:
    - **Script**: Loads the ChatGPT Builder plugin and initializes the chatbot with specific settings.

## Usage

### Embedding the Chatbot

The chatbot is embedded using the  Builder plugin. Below is a breakdown of the configuration:

- **Script Source**: The script is sourced from `https://app.chatgptbuilder.io/webchat/plugin.js`.
- **Configuration**: 
  - `pageId`: Set to `1708308`, identifying the specific chatbot page.
  - `color`: The chatbot's primary color is set to `#007BFF`, a shade of blue.
  - `loadMessages`: Set to `false`, meaning the chatbot does not load previous messages.
  - `template`: The chatbot uses "template1" for its interface design.

### Customization

You can customize the chatbot by modifying the script's configuration:

- **pageId**: Change this to load a different chatbot.
- **color**: Adjust the color to match your website's theme.
- **loadMessages**: Set to `true` if you want the chatbot to load previous messages.
- **template**: Choose a different template for the chatbot interface.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

