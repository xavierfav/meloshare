import os
import logging

log = logging.getLogger(__name__)

def register_blueprints(app, blueprints):
    """Register all Flask blueprints with our Flask app.

    Args:
        app: The Flask application.
        blueprints (list): A list of tuple (blueprint, path).
    """
    for bp, path in blueprints:
        try:
            app.register_blueprint(bp, url_prefix=path)
            log.info("Blueprint registered: %s --> %s" % (bp, path))
        except Exception as e:
            log.error("Error registering blueprint %s --> %s" % (bp, path))
    log.debug("Registered %s blueprints" % len(blueprints))
    log.info("URL Map: %s" % app.url_map)

def register_extensions(app, extensions):
    """Register all Flask extensions with our Flask app.

    Args:
        app: The Flask application.
        extensions (list): A list of Flask Flash resources.
    """
    for e in extensions:
        if isinstance(e, tuple):
            log.info("Registering extension: %s" % e[0])
            log.info("Extension config: %s" % e[1])
            kwargs = e[1]
            e = e[0]
        else:
            log.info("Registering extension: %s" % e)
            kwargs = {}
        e.init_app(app, **kwargs)
