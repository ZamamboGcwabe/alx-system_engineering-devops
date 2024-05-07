# Execute a command

exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/bin/ps -ef | /grep killmenow | /grep -v grep >/dev/null 2>&1',
}
