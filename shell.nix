{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # Specify the packages you need
  buildInputs = [
    pkgs.python311  # Use Python 3.11 (or another version if preferred)
    pkgs.python311Packages.requests  # Python requests library
    pkgs.python311Packages.twilio    # Python twilio library
  ];

  # Set up the environment (optional)
  shellHook = ''
    echo "Welcome to the endpoint monitoring environment!"
    echo "Python version: $(python --version)"
    echo "Installed packages:"
    pip list
  '';
}