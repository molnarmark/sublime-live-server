<p align="center">
  <img src="images/logo.png">
  <h4 align="center">Launch a Development Server directly from Sublime Text!</h4>
</p>

## 📋 Introduction

This package integrates the **[Live Server](https://www.npmjs.com/package/live-server)** Node package, giving the ability to launch a local development server to serve content directly from Sublime Text.

<p align="center">
  <b>For this package to work, you need to have a folder opened inside your editor. That will be the root path the server starts serving on.</b>
</p>

#### 💡 About Live Server:

**[Live Server](https://www.npmjs.com/package/live-server)** is Node.js tool that spins up a local development server in the given directory.

It features live browser reloading, which simply means that your browser will automatically refresh the page when any change is made to your HTML & CSS files.

Useful for static sites, SPAs, and general HTML/CSS fiddling.

## ❗Prerequisites

You need the following software installed to use **Live Server**.

- [**`Node.js`**](https://nodejs.org/)
- [**`npm`**](https://npmjs.com) or [**`Yarn`**](https://yarnpkg.com)
- [**`Live Server`**](https://www.npmjs.com/package/live-server) installed globally

To install Live Server globally using **`npm`**, run:

```sh
npm install -g live-server
```

To install Live Server globally using **`Yarn`**, run:

```sh
yarn global add live-server
```

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

## ❓ Usage

This package exposes 3 commands that can be used directly via the Command Palette, or bound to keys. These are:

**`Live Server: Start`**

- Maps to `live_server_start`

**`Live Server: Stop`**

- Maps to `live_server_stop`

**`Live Server: Open In Browser`**

- Maps to `live_server_open_in_browser`

Status bar messages with indicator emojis are implemented into the package, displaying information in cases such as:

- 🎉 Live Server running
- ❌ Live Server stopped
- ✔️ Live Server status

When the development server is running, a status message will be shown in the status bar indicating that the server is running.
This is shared across all views in the opened instance.

<p align="center">
  <img src="images/statusbar.png">
</p>

## 🔨 Settings

To change your settings, bring up the Command Palette and select: **`Preferences: Live Server Settings`**

The default settings are the following:

```js
// Note: These are just mappings to https://github.com/tapio/live-server#usage-from-command-line
{
  "node_executable_path": "/usr/bin/node",
  "global_node_modules_path": "/usr/local/lib/node_modules",
  "port": 8080,
  "address": "localhost",
  "cors": true,
  "browser": "default",
  "nobrowser": false,
  "wait": 100
}
```

#### **`node_executable_path`**

- Path to the Node runtime executable. You can run **`whereis node`** in your terminal to find this.
- ##### **`default: /usr/bin/node`**

#### **`global_node_modules_path`**

- Path to the default **node_modules** directory. You can run **`npm root -g`** or **`yarn global bin`** in your terminal to find this.
- ##### **`default: /usr/local/lib/node_modules`**

#### **`port`**

- The default port for the server.
- ##### **`default: 8080`**

#### **`address`**

- Host address. This should always be either localhost or 127.0.0.1.
- ##### **`default: localhost`**

#### **`cors`**

- Enables CORS for any origin.
- ##### **`default: true`**

#### **`browser`**

- Specifies which browser to use.
- Valid values are:

  - **`default`**
  - **`google-chrome`**
  - **`firefox`**

- ##### **`default: default`**

#### **`nobrowser`**

- By setting this to true, the browser will not open the server by default
- ##### **`default: false`**

#### **`wait`**

- Wait this amount of milliseconds before reloading the page after a change
- ##### **`default: 100`**

## 🔖 Credits

- This package wouldn't exist without the amazing [**`Node`**](https://nodejs.org/) package also called **[Live Server](https://www.npmjs.com/package/live-server)** by **[Tapio Vierros](https://github.com/tapio)**.
