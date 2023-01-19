# cerberus-testnet

# inferno-1
Version of cerberus: v3.0.1

chain-id=inferno-1

[config.toml]
persistent_peers = "19e2d641658c6e25198c7ecb5a936db283b46a34@116.202.143.90:26656"


#timeout_commit: Please set it up to 29s. I took spare machines with small disks at the moment. We can accelerate later on when we are all onboarded and ready for the votings. 

timeout_commit = "29s"

[app.toml]
#please make sure you're running with this line:
iavl-disable-fastnode = false

## instructions for old validators of inferno-1, so you can re-use your node


```
sudo systemctl stop cerberusd
rm -rf ~/cerberus
git clone https://github.com/windpowerstake/cerberus
cd cerberus/
git checkout v3.0.1
make install

cd ~
rm -rf ~/.cerberus/
cerberusd init "yourMonikerNode" --chain-id "inferno-1"
```


Make sure your version is ok:

```cerberusd version```


Must return v3.0.1


## An automation to put your peers in your config.toml file:

```
peers="19e2d641658c6e25198c7ecb5a936db283b46a34@116.202.143.90:26656"
sed -i.bak -e "s/^persistent_peers *=.*/persistent_peers = \"$peers\"/" ~/.cerberus/config/config.toml
```

Make sure the persistent peer is: `19e2d641658c6e25198c7ecb5a936db283b46a34@116.202.143.90:26656`

If this does not work do it manually.

## Reload the genesis for inferno-1

Get your genesis.json file from discord or from here: https://github.com/windpowerstake/cerberus-testnet/blob/main/genesis.json

Or just with the command:

```
#download genesis
rm ~/.cerberus/config/genesis.json
wget https://raw.githubusercontent.com/windpowerstake/cerberus-testnet/main/genesis.json -P ~/.cerberus/config/
```

Verify the shasum:
``` 
jq -S -c -M '' ~/.cerberus/config/genesis.json | sha256sum
#returns 7bfb02dff80781fdf030b02c974a797ebbd8bd0e5ebab06e3544ff32c13cdc2f  -
```


When you are ready, make sure to enable cerberus as a daemon (service) and start the service.


testnet is up, ask for tokens in the testnet channel
