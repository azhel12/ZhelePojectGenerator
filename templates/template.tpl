// Define target cpu frequence. Used for delay, configure flash latency
#define F_CPU {{F_CPU}}

{% if ConfigureClock != "" %}#include <clock.h>{% endif %}
{% if ConfigureGPIO != "" %}#include <iopins.h>{% endif %}
{% if ConfigureSPI != "" %}#include <spi.h>{% endif %}

{% if ConfigureClock != "" %}using namespace Zhele::Clock;{% endif %}
{% if ConfigureGPIO != "" %}using namespace Zhele::IO;{% endif %}

{% if ConfigureClock != "" %}void ConfigureClock();{% endif %}
{% if ConfigureGPIO != "" %}void ConfigureGPIO();{% endif %}
{% if ConfigureSPI != "" %}void ConfigureSPI();{% endif %}

int main()
{
	{% if ConfigureClock != "" %}ConfigureClock();{% endif %}
	{% if ConfigureGPIO != "" %}ConfigureGPIO();{% endif %}
	{% if ConfigureSPI != "" %}ConfigureSPI();{% endif %}
	
	for (;;)
	{
	}
}

{{ConfigureClock}}

{{ConfigureGPIO}}

{{ConfigureSPI}}