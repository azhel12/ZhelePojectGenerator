void ConfigureUsart()
{
    {% if 'USART1' in USART_Conf.keys() %}//Usart1 setup

    //Select pin {{USART_Conf['USART1']['TX']}} as TX, {{USART_Conf['USART1']['RX']}} as RX on Usart1
    Usart1::SelectTxRxPins<{{USART_Conf['USART1']['TX']}},{{USART_Conf['USART1']['RX']}}>();{% endif %}
    {% if 'USART2' in USART_Conf.keys() %}//Usart2 setup

    //Select pin {{USART_Conf['USART1']['TX']}} as TX, {{USART_Conf['USART1']['RX']}} as RX on Usart2
    Usart2::SelectTxRxPins<{{USART_Conf['USART2']['TX']}},{{USART_Conf['USART2']['RX']}}>();{% endif %}
    {% if 'USART3' in USART_Conf.keys() %}
    //Usart3 setup

    //Select pin {{USART_Conf['USART1']['TX']}} as TX, {{USART_Conf['USART1']['RX']}} as RX on Usart3
    Usart3::SelectTxRxPins<{{USART_Conf['USART3']['TX']}},{{USART_Conf['USART3']['RX']}}>();{% endif %}
    {% if 'USART4' in USART_Conf.keys() %}
    //Usart4 setup

    //Select pin {{USART_Conf['USART1']['TX']}} as TX, {{USART_Conf['USART1']['RX']}} as RX on Usart4
    Usart4::SelectTxRxPins<{{USART_Conf['USART4']['TX']}},{{USART_Conf['USART4']['RX']}}>();{% endif %}
}