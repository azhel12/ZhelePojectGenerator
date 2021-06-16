// Define target cpu frequence. Used for delay, configure flash latency
#define F_CPU {{F_CPU}}

{% if ConfigureClock != "" %}#include <clock.h>{% endif %}
{% if ConfigureGPIO != "" %}#include <iopins.h>{% endif %}
{% if ConfigureSPI != "" %}#include <spi.h>{% endif %}
{% if ConfigureI2C != "" %}#include <i2c.h>{% endif %}
{% if ConfigureUsart != "" %}#include <usart.h>{% endif %}

using namespace Zhele;
{% if ConfigureClock != "" %}using namespace Zhele::Clock;{% endif %}
{% if ConfigureGPIO != "" %}using namespace Zhele::IO;{% endif %}
{% if ConfigureSPI != "" %}using namespace Zhele::Private;{% endif %}

{% if ConfigureClock != "" %}void ConfigureClock();{% endif %}
{% if ConfigureGPIO != "" %}void ConfigureGPIO();{% endif %}
{% if ConfigureSPI != "" %}void ConfigureSPI();{% endif %}
{% if ConfigureI2C != "" %}void ConfigureI2c();{% endif %}
{% if ConfigureUsart != "" %}void ConfigureUsart();{% endif %}

int main()
{
	{% if ConfigureClock != "" %}ConfigureClock();{% endif %}
	{% if ConfigureGPIO != "" %}ConfigureGPIO();{% endif %}
	{% if ConfigureSPI != "" %}ConfigureSPI();{% endif %}
	{% if ConfigureI2C != "" %}ConfigureI2c();{% endif %}
	{% if ConfigureUsart != "" %}ConfigureUsart();{% endif %}
	
	for (;;)
	{
	}
}

{{ConfigureClock}}

{{ConfigureGPIO}}

{{ConfigureSPI}}

{{ConfigureI2C}}

{{ConfigureUsart}}