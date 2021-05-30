void ConfigureSPI()
{
	{% for SpiInterface in SPI_Conf.keys() %}// {{SpiInterface}} setup
	{% if 'BaudRatePrescaler' in SPI_Conf[SpiInterface] %}// Init {{SpiInterface}} with divider {{SPI_Conf[SpiInterface]['BaudRatePrescaler']}}
	Init(SpiBase::ClockDivider::Div{{SPI_Conf[SpiInterface]['BaudRatePrescaler']}});{% else %}// Init {{SpiInterface}}
	Init();{% endif %}
	{% if 'DataSize' in SPI_Conf[SpiInterface] %}// Set Spi data size as DataSize{{SPI_Conf[SpiInterface]['DataSize']}}
	Spi::SetDataSize(SpiBase::DataSize::DataSize{{SPI_Conf[SpiInterface]['DataSize']}});{% endif %}
	{% if 'FirstBit' in SPI_Conf[SpiInterface] %}{% if SPI_Conf[SpiInterface]['FirstBit'] == 'LSB' %}// Set bit order as LSB
	Spi::SetBitOrder(SpiBase::BitOrder::LsbFirst);{% endif %}{% if SPI_Conf[SpiInterface]['FirstBit'] == 'MSB' %}// Set bit order as MSB
	Spi::SetBitOrder(SpiBase::BitOrder::MsbFirst);{% endif %}{% endif %}
 	{% if 'Phase' in SPI_Conf[SpiInterface] %}{% if SPI_Conf[SpiInterface]['Phase'] == '1' %}// Set clock phase as Leading
	Spi::SetClockPhase(SpiBase::ClockPhase::ClockPhaseLeadingEdge);{% endif %}{% if SPI_Conf[SpiInterface]['Phase'] == '2' %}// Set clock phase as Falling
	Spi::SetClockPhase(SpiBase::ClockPhase::ClockPhaseFallingEdge);{% endif %}{% endif %}
	{% if 'Polarity' in SPI_Conf[SpiInterface] %}{% if SPI_Conf[SpiInterface]['Polarity'] == 'HIGH' %}// Set clock polarity high
	Spi::SetClockPolarity(SpiBase::ClockPolarity::ClockPolarityHigh);{% endif %}{% if SPI_Conf[SpiInterface]['Polarity'] == 'LOW' %}// Set clock polarity low
	Spi::SetClockPolarity(SpiBase::ClockPolarity::ClockPolarityLow);{% endif %}{% endif %}
 	{% endfor %}
}
