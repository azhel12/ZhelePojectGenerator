void ConfigureI2c()
{
    {% for Interface in I2C_Conf.keys() %}// {{Interface}} setup
    {% if 'ClockSpeed' in I2C_Conf[Interface] %}// Init {{Interface}}
    {{Interface}}::Init({{I2C_Conf[Interface]['ClockSpeed']}}000U);{% else %}// Init {{Interface}}
    {{Interface}}::Init();{% endif %}// Select pin {{I2C_Conf[Interface]['SCL']}} as SCL, {{I2C_Conf[Interface]['SDA']}} as SDA
    {{Interface}}::SelectPins<{{I2C_Conf[Interface]['SCL']}}, {{I2C_Conf[Interface]['SDA']}}>();
    {% endfor %}
}