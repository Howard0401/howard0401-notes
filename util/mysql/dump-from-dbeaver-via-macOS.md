
# dump-from-dbeaver-via-macOS
紀錄 mysql 用 dbeaver dump 的簡易步驟與快捷鍵坑 
# steps

```shell
brew install mysql-client@5.7
where mysql # /opt/homebrew/opt/mysql@5.7/bin/mysql
brew services start mysql@5.7
brew services list # make sure server running
```

``` 
# dbeaver
## press shift+cmd+G to locate #/opt/homebrew/opt/mysql@5.7/bin/mysql
choose mysql-client-local folder, select dump options
## that's all
```
