# Usage

## Production

First you need to define the environment variables:
```shell
# RabbitMQ URL.
$ export BROKER_URL="amqp://some_user:some_password:127.0.0.1"

# Redis URL.
$ export RESULT_BACKEND="redis://127.0.0.1"
```

### Using init.d

- Copy the `init.d/drupsd` file into `/etc/init.d/drupsd`
- Modify and copy the `init.d/drupsd.config.example` file to `/etc/default/drups` (or `/usr/local/etc/drups` on `BSD`)
- Run the daemon `sudo /etc/init.d/drupsd start`. It is important to run it with the `root` user

The default user and group for running the `drupsd` daemon is `drups:drups`. You should create it first (or change the
default user in `/etc/default/drups` -> `DRUPSD_USER` and `DRUPSD_GROUP`).

#### Available command for drups daemon

- `start` - Start the daemon
- `stop` - Stop the daemon
- `restart` - Restart the daemon
- `status` - Get the daemon status
- `kill` - Kill the daemon
- `dryrun` - Start the daemon in verbose mode

### Using celery

```shell
$ celery -A drups worker --loglevel=INFO -E
```

## Development

- Create the `.env.local` file and set the environment variables:
    ```
    # Example .env.local

    # RabbitMQ URL.
    BROKER_URL = 'amqp://some_user:some_password:127.0.0.1'

    # Redis URL.
    RESULT_BACKEND = 'redis://127.0.0.1'
    ```

- Run the Celery worker
    ```shell
    $ celery -A drups.app worker --loglevel=INFO -E
    ```
