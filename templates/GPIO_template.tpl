void ConfigureGPIO()
{
{% for portName in GPIO_Conf.keys() %}
	{% if 'Label' in GPIO_Conf[portName] %}// {{GPIO_Conf[portName]['Label']}} configuration{% else %}// {{portName}} configuration{% endif %}
	
	// Enable port clocking
	{{portName}}::Port::Enable();
	// Configure as {{GPIO_Conf[portName]['Conf']}} pin
	{{portName}}::SetConfiguration({{portName}}::Configuration::{{GPIO_Conf[portName]['Conf']}});
	{% if 'GPIO_Mode' in GPIO_Conf[portName].keys() %}{% if GPIO_Conf[portName]['GPIO_Mode'] == 'PP' %}// Set driver type as push-pull
	{{portName}}::SetDriverType({{portName}}::DriverType::PushPull);{% else %}// Set driver type as opendrain
	{{portName}}::SetDriverType({{portName}}::DriverType::OpenDrain);{% endif %}{% endif %}	
	{% if 'GPIO_Speed' in GPIO_Conf[portName].keys() %}{% if GPIO_Conf[portName]['GPIO_Speed'] == 'HIGH' %}// Set speed as fast
	{{portName}}::SetSpeed({{portName}}::Speed::Fast);{% endif %}{% if GPIO_Conf[portName]['GPIO_Speed'] == 'MEDIUM' %}// Set speed as medium
	{{portName}}::SetSpeed({{portName}}::Speed::Medium);{% endif %}{% if GPIO_Conf[portName]['GPIO_Speed'] == 'LOW' %}// Set speed as slow
	{{portName}}::SetSpeed({{portName}}::Speed::Slow){% endif %}{% endif %}
	{% if 'PuPd' in GPIO_Conf[portName].keys() %}{% if GPIO_Conf[portName]['PuPd'] == 'PULLUP' %}// Set pull-mode as pull-up
	{{portName}}::SetPullMode({{portName}}::PullMode::PullUp);{% endif %}{% if GPIO_Conf[portName]['PuPd'] == 'PULLDOWN' %}// Set pull-mode as pull-down
	{{portName}}::SetPullMode({{portName}}::PullMode::PullDown);{% endif %}{% if GPIO_Conf[portName]['PuPd'] == 'NOPULL' %}// Set pull-mode as no-pull
	{{portName}}::SetPullMode({{portName}}::PullMode::NoPull);{% endif %}{% endif %}
{% endfor %}	
}
