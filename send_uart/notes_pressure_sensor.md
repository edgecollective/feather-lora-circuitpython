with the potted pressure sensor, connect green to 'RX' on feather, and yellow (unused) to 'TX'

note that i seem to need to read the uart faster than the rate at which the pressure sensor is sending its data over the uart, or else I get truncated lines

