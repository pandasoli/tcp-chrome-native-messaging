This codes creates a TCP server in the native-messaging host and
sends the received message to the extension.

Remember to:
- Update `"allowed_origins"` and `"path"` in [`./host/com.elisoli.nekovim.discord.json`](./host/com.elisoli.nekovim.discord.json).
- Run [`./host/install`](./host/install) to register the host.
- Run `npm i` inside [`./extension/`](./extension/)
