# Installing flask

class { 'python::pip': }

package { 'Flask':
  ensure => present,
  provider => 'pip',
  require => Class['python::pip'],
  version => '2.1.0',
}
