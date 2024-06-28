# This Puppet manifest kills the process named 'killmenow' using pkill

exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => 'pgrep killmenow',
}

