// Define target cpu frequence. Used for delay, configure flash latency
#define F_CPU 20000000

#include <clock.h>
#include <iopins.h>
#include <spi.h>

using namespace Zhele::Clock;
using namespace Zhele::IO;

void ConfigureClock();
void ConfigureGPIO();
void ConfigureSPI();

int main()
{
	ConfigureClock();
	ConfigureGPIO();
	ConfigureSPI();
	
	for (;;)
	{
	}
}

void ConfigureClock()
{
    
    
    // Set clock sourse as Pll
    SysClock::SelectClockSource(SysClock::Pll);
    
    
    // Set PllDivider value
    PllClock::SetDevider();
    //Set Multiplier
    PllClock::SetMultiplier();
    // Set Ahb prescaler value
    AhbClock::SetPrescaler(Prescaler::Div4);
    // Set Apb1 prescaler value
    Apb1Clock::SetPrescaler(Apb1Clock::Div4);
    
}

void ConfigureGPIO()
{

	// tewrwwwrew configuration
	
	// Enable port clocking
	Pa3::Port::Enable();
	// Configure as In pin
	Pa3::SetConfiguration(Pa3::Configuration::In);
		
	
	// Set pull-mode as pull-up
	Pa3::SetPullMode(Pa3::PullMode::PullUp);

	// Pa2 configuration
	
	// Enable port clocking
	Pa2::Port::Enable();
	// Configure as Out pin
	Pa2::SetConfiguration(Pa2::Configuration::Out);
	// Set driver type as opendrain
	Pa2::SetDriverType(Pa2::DriverType::OpenDrain);	
	// Set speed as slow
	Pa2::SetSpeed(Pa2::Speed::Slow)
	// Set pull-mode as pull-up
	Pa2::SetPullMode(Pa2::PullMode::PullUp);

	// Pa1 configuration
	
	// Enable port clocking
	Pa1::Port::Enable();
	// Configure as Out pin
	Pa1::SetConfiguration(Pa1::Configuration::Out);
	// Set driver type as push-pull
	Pa1::SetDriverType(Pa1::DriverType::PushPull);	
	// Set speed as slow
	Pa1::SetSpeed(Pa1::Speed::Slow)
	// Set pull-mode as pull-up
	Pa1::SetPullMode(Pa1::PullMode::PullUp);
	
}

void ConfigureSPI()
{
	// SPI1 setup
	// Init SPI1
	Init();
	// Set Spi data size as DataSize6
	Spi::SetDataSize(SpiBase::DataSize::DataSize6);
	// Set bit order as LSB
	Spi::SetBitOrder(SpiBase::BitOrder::LsbFirst);
 	// Set clock phase as Falling
	Spi::SetClockPhase(SpiBase::ClockPhase::ClockPhaseFallingEdge);
	// Set clock polarity high
	Spi::SetClockPolarity(SpiBase::ClockPolarity::ClockPolarityHigh);
 	
}