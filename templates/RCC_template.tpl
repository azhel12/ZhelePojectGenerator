void ConfigureClock()
{
    {% if RCC_Conf['SystemClock'] == 'HSE' %}// Set clock sourse as HSE
    SysClock::SelectClockSource(SysClock::HSE);{% endif %}
    {% if RCC_Conf['SystemClock'] == 'HSI' %}// Set clock sourse as HSI
    SysClock::SelectClockSource(SysClock::HSI);{% endif %}
    {% if RCC_Conf['SystemClock'] == 'PLLCLK' %}// Set clock sourse as Pll
    SysClock::SelectClockSource(SysClock::Pll);
    {% if RCC_Conf['clockSource'] == 'External' %}// Select HSE as PLL source
    PllClock::SelectClockSource(PllClock::External);{% endif %}
    {%if RCC_Conf['clockSource'] == 'Internal' %}// // Select HSI as PLL source
    PllClock::SelectClockSource(PllClock::Internal);{% endif %}
    {% if 'PLLM' in RCC_Conf.keys() %}// Set PLLM value
    PllClock::SetDivider({{RCC_Conf['PLLM']}});
    {% elif 'PLLDivider' in RCC_Conf.keys() %}// Set PllDivider value
    PllClock::SetDevider({{RCC_Conf['PLLDivider']}});{% endif %}
    {% if 'PLLN' in RCC_Conf.keys() %}// Set PLLN value
    PllClock::SetMultiplier({{RCC_Conf['PLLN']}});{% else %}//Set Multiplier
    PllClock::SetMultiplier({{RCC_Conf['Multiplier']}});{% endif %}{% endif %}
    {% if 'AHBPrescaler' in RCC_Conf.keys() %}// Set Ahb prescaler value
    AhbClock::SetPrescaler(AhbClock::Div{{RCC_Conf['AHBPrescaler']}});{% endif %}
    {% if 'APB1Prescaler' in RCC_Conf.keys() %}// Set Apb1 prescaler value
    Apb1Clock::SetPrescaler(Apb1Clock::Div{{RCC_Conf['APB1Prescaler']}});{% endif %}
    {% if 'APB2Prescaler' in RCC_Conf.keys() %}// Set Apb2 prescaler value
    Apb2Clock::SetPrescaler(Apb2Clock::Div{{RCC_Conf['APB2Prescaler']}});{% endif %}
}
