<p align="center">
  <img src="images/logo.png">
</p>

## 📋 Introduction

This package integrates the **[Live Server](http://google.com)** package, giving the ability to launch a local development server to serve content directly from Sublime Text.

## 🌀 Installation

#### Package Control

Live Server is currently awaiting to be added to **Package Control**.

[comment]: <> (This package is available in Package Control under the name **Live Server**.)

#### As a Repository

If this package isn't on Package Control at the time you are trying to install it,

- Bring up the Command Palette
- Select **`Package Control: Add Repository`**
- Paste https://github.com/molnarmark/sublime-live-server
- Press Enter

## 🔨 Settings

The default settings are the following:

```json
// Note: These are just mappings to https://github.com/tapio/live-server#usage-from-command-line
{
  "node_executable_path": "/usr/bin/node",
  "global_node_modules_path": "/usr/local/lib/node_modules",
  "port": "8080",
  "address": "localhost",
  "cors": true,
  "ignore": ""
}
```

### **`node_executable_path`**

- Path to the Node runtime executable. You can run **`whereis node`** in your terminal to find this.
- ##### **`default: /usr/bin/node`**

### **`global_node_modules_path`**

- Path to the default **node_modules** directory. You can run **`npm root -g`** in your terminal to find this.
- ##### **`default: /usr/local/lib/node_modules`**

### **`port`**

- The default port for the server.
- ##### **`default: 8080`**

### **`address`**

- Host address. This should always be either localhost or 127.0.0.1.
- ##### **`default: localhost`**

### **`cors`**

- Enables CORS for any origin.
- ##### **`default: true`**

### **`ignore`**

- Regular Expression to ignore specific files & folders.
- ##### **`default: ""`**

## 🔖 Credits

- This package wouldn't exist without the amazing Node package also called **[Live Server](http://google.com)** by **[Tapio Vierros](https://github.com/tapio)**.

```

```
