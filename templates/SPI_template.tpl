void ConfigureSPI()
{
	{% for SpiInterface in SPI_Conf.keys() %}// {{SpiInterface}} setup
	{% if 'BaudRatePrescaler' in SPI_Conf[SpiInterface] %}// Init {{SpiInterface}} with divider {{SPI_Conf[SpiInterface]['BaudRatePrescaler']}}
	{{SpiInterface}}::Init(SpiBase::ClockDivider::Div{{SPI_Conf[SpiInterface]['BaudRatePrescaler']}});{% else %}// Init {{SpiInterface}}
	{{SpiInterface}}::Init();{% endif %}
	{{SpiInterface}}::SelectPins<{{SPI_Conf[SpiInterface]['MOSI']}}, {{SPI_Conf[SpiInterface]['MISO']}}, {{SPI_Conf[SpiInterface]['CLK']}}, {{SPI_Conf[SpiInterface]['NSS']}}>();
	{% if 'DataSize' in SPI_Conf[SpiInterface] %}// Set Spi data size as DataSize{{SPI_Conf[SpiInterface]['DataSize']}}
	{{SpiInterface}}::SetDataSize(SpiBase::DataSize::DataSize{{SPI_Conf[SpiInterface]['DataSize']}});{% endif %}
	{% if 'FirstBit' in SPI_Conf[SpiInterface] %}{% if SPI_Conf[SpiInterface]['FirstBit'] == 'LSB' %}// Set bit order as LSB
	{{SpiInterface}}::SetBitOrder(SpiBase::BitOrder::LsbFirst);{% endif %}{% if SPI_Conf[SpiInterface]['FirstBit'] == 'MSB' %}// Set bit order as MSB
	{{SpiInterface}}::SetBitOrder(SpiBase::BitOrder::MsbFirst);{% endif %}{% endif %}
	{% if 'Polarity' in SPI_Conf[SpiInterface] %}{% if SPI_Conf[SpiInterface]['Polarity'] == 'HIGH' %}// Set clock polarity high
	{{SpiInterface}}::SetClockPolarity(SpiBase::ClockPolarity::ClockPolarityHigh);{% endif %}{% if SPI_Conf[SpiInterface]['Polarity'] == 'LOW' %}// Set clock polarity low
	{{SpiInterface}}::SetClockPolarity(SpiBase::ClockPolarity::ClockPolarityLow);{% endif %}{% endif %}
 	{% if 'Phase' in SPI_Conf[SpiInterface] %}{% if SPI_Conf[SpiInterface]['Phase'] == '1' %}// Set clock phase as Leading
	{{SpiInterface}}::SetClockPhase(SpiBase::ClockPhase::ClockPhaseLeadingEdge);{% endif %}{% if SPI_Conf[SpiInterface]['Phase'] == '2' %}// Set clock phase as Falling
	{{SpiInterface}}::SetClockPhase(SpiBase::ClockPhase::ClockPhaseFallingEdge);{% endif %}{% endif %}
 	{% endfor %}
}
