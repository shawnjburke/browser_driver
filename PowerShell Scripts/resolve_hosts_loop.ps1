$start_time = (Get-date)
$seconds_to_sleep = 5
$host_list = @("www.docmagic.com","www.loan-magic.com","smartclose.docmagic.com","download.docmagic.com","www.documentexpressinc.com")

$kill_help = "Type CTRL+C to Terminate..."
$kill_help_count = 0
Try {
	While($true) {
		# Print the help every 8th itteration
		if (!($kill_help_count%8)) {
			Write-Host $kill_help
		}
		$kill_help_count += 1
		
		# Test all the hosts in our lists
		foreach ($host_name in $host_list) {
			$ip_list = [System.Net.Dns]::GetHostAddresses($host_name)
			# Each host may have multiple IP addresses, display them all
			foreach ($ip_address in $ip_list) {
				$time_stamp = Get-Date	
				Write-Host "$($time_stamp) $($host_name) resolves to $($ip_address.IPAddressToString)"
				
			}
		}
		# Write a blank line for better display.
		Write-Host ""
		Start-Sleep -s $seconds_to_sleep
	}
}
Finally {
	$end_time = (Get-date)
	$time_diff = $end_time - $start_time
	Write-Host "Process ran for $($time_diff)"
}