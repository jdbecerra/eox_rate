###

from django.apps import AppConfig

class EoxRateAppConfig(AppConfig):

    name = 'eox_rate'

    plugin_app = {

	'url_config': {
	
	    'lms.djangoapp': {
                'namespace': 'eox_rate',
                'regex': r'^eox_rate/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'eox_rate',
                'regex': r'^eox_rate/',
                'relative_path': 'urls',
            }

	},
	'settings_config': {

	    'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'production': {'relative_path': 'settings.production'},
            },

	},
	'signals_config': {

	    'lms.djangoapp':{
		'relative_path': 'my_signals',
		'receivers': [{
		    'receiver_func_name': 'on_signal_x',
		    'signal_path': 'full_path_to_signal_x_module.SignalX',
		    'dispatch_uid': 'eox_rate.my_signals.on_signal_x',
   		    'sender_path': 'full_path_to_sender_app.ModelZ',	

		}],
	    }
	},
	'view_context_config': {
	     'lms.djangoapp': {
		'course_dashboard': 'eox_rate.context_api.get_dashboard_context'
	     }
	}

    }
