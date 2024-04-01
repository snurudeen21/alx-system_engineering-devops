# install Flask using puppet

exec { 'install_flask':
  command  => '/usr/bin/pip3 install Flask==2.1.0',
  unless   => '/usr/bin/pip3 show Flask | grep -q "Version: $(URI::encode_www_form_component("2.1.0"))"',
  provider => 'shell',
}
