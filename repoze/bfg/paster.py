from paste.script.templates import Template
from paste.util.template import paste_script_template_renderer

class StarterProjectTemplate(Template):
    _template_dir = 'paster_templates/starter'
    summary = 'repoze.bfg starter project'
    template_renderer = staticmethod(paste_script_template_renderer)

class ZODBProjectTemplate(Template):
    _template_dir = 'paster_templates/zodb'
    summary = 'repoze.bfg ZODB starter project'
    template_renderer = staticmethod(paste_script_template_renderer)

class RoutesAlchemyProjectTemplate(Template):
    _template_dir = 'paster_templates/routesalchemy'
    summary = 'repoze.bfg SQLAlchemy project using Routes (no traversal)'
    template_renderer = staticmethod(paste_script_template_renderer)

class AlchemyProjectTemplate(Template):
    _template_dir = 'paster_templates/alchemy'
    summary = 'repoze.bfg SQLAlchemy project using traversal'
    template_renderer = staticmethod(paste_script_template_renderer)
