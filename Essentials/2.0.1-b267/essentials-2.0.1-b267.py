from mcresolver.scripts import *
import os

_plugin_versions_ = ['2.0.1-b267']
_plugin_id_ = "9089"  # Spigot resource ID

__config_template__ = "https://raw.githubusercontent.com/TechnicalBro/minecraft-plugin-config-templates/master/Essentials/2.0.1-b267/essentials-template.yml"
__config_defaults__ = "https://raw.githubusercontent.com/TechnicalBro/minecraft-plugin-config-templates/master/Essentials/2.0.1-b267/essentials-defaults.yml"


def configure(parent_folder, config_options={}, **kwargs):
    commons_folder = os.path.join(parent_folder, 'Essentials')

    if not os.path.exists(commons_folder):
        os.makedirs(commons_folder)

    # Get the default configuration values for Commons, incase some aren't present in the options.
    defaults = get_configuration_defaults(url=__config_defaults__)

    # Create a full dictionary of all the options required to render the template, merging
    # in the missing values from the default config.
    options = merge_configuration_options(config_options, defaults)
    config_file = os.path.join(commons_folder, 'config.yml')

    essentials_config = render_config_from_url(__config_template__, options)
    # Lastly write the configuration to the file specified!
    write_file(config_file, essentials_config)
    print("Configuration for Essentials has been rendered!")
