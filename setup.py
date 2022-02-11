###

from setuptools import setup
setup(

   entry_points={
	"lms.djangoapp": [
	   "eox_rate = eox_rate.apps:EoxRateAppConfig",
	],
	"cms.djangoapp": [
	   "eox_rate = eox_rate.apps:EoxRateAppConfig",
	],
   }
)
