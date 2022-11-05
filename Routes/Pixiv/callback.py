# -*- coding: utf8 -*-
# import json
base = '''<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <link rel="icon" type="image/ico" href="https://d.sirin.top/tmp_crop_decode.jpg">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="renderer" content="webkit" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0,maximum-scale=5.0">
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    <title>幻海API</title>
    <meta name="description" content="currentItem.description" />
    <link rel="preconnect" href="//d.sirin.top">
    <link rel="preconnect" href="//fastly.jsdelivr.net">
    <link rel="stylesheet" href="https://fastly.jsdelivr.net/npm/mdui@1.0.2/dist/css/mdui.min.css"/>
    <link rel="stylesheet" href="https://d.sirin.top/api/index.css">
    <script src="https://fastly.jsdelivr.net/npm/mdui@1.0.2/dist/js/mdui.min.js"></script>
    <script src="https://d.sirin.top/api/index.js"></script>
<body class="
    mdui-drawer-body-left
    mdui-appbar-with-toolbar
    mdui-theme-primary-indigo
    mdui-theme-accent-pink
    mdui-theme-layout-dark" id="p-d">
    <script>
          function getCookie(name) {
            var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
            if (arr != null) return (arr[2]); return null;

          }
          function change_color() {
            document.body.classList.remove("mdui-theme-primary-indigo")
            document.body.classList.remove("mdui-theme-accent-pink")
            document.body.classList.remove("mdui-theme-layout-dark")
            document.body.classList.add("mdui-theme-layout-" + getCookie("docs-theme-layout"));
            document.body.classList.add("mdui-theme-primary-" + getCookie("docs-theme-primary"));
            document.body.classList.add("mdui-theme-accent-" + getCookie("docs-theme-accent"));
          }
          (function color() { change_color(); }());
        </script>


    <header class="appbar mdui-appbar mdui-appbar-fixed">
        <div class="mdui-toolbar mdui-color-theme">
            <span class="mdui-btn mdui-btn-icon mdui-ripple mdui-ripple-white"
                mdui-drawer="{target: '#main-drawer', swipe: true}">
                <i class="mdui-icon material-icons">menu</i>
            </span>
            <a href="/release/API/" class="mdui-typo-headline mdui-hidden-xs">幻海实验室</a>
            <a href="/release/API/" class="mdui-typo-title">API</a>
            <div class="mdui-toolbar-spacer"></div>
            <span class="mdui-btn mdui-btn-icon mdui-ripple mdui-ripple-white"
                mdui-dialog="{target: '#dialog-docs-theme'}" mdui-tooltip="{content: '设置主题'}">
                <i class="mdui-icon material-icons">color_lens</i>
            </span>        </div>
        </header>
    <div class="mdui-drawer" id="main-drawer">
    <div class="mdui-list" mdui-collapse="{accordion: true}" style="margin-bottom: 76px;">
      <div class="
                mdui-collapse-item
                ">
        <div class="mdui-collapse-item-header mdui-list-item mdui-ripple">
          <i class="
                    mdui-list-item-icon
                    mdui-icon
                    material-icons
                    mdui-text-color-blue">near_me</i>
          <div class="mdui-list-item-content">开始使用</div>
          <i class="mdui-collapse-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
        </div>
        <div class="mdui-collapse-item-body mdui-list">
          <a href="/release/API/introduction" class="
                          mdui-list-item
                          mdui-ripple
                          ">简介</a><a href="/release/API/download" class="
                          mdui-list-item
                          mdui-ripple
                          ">下载</a>
        </div>
      </div>
      <div class="
                mdui-collapse-item
                ">
        <div class="mdui-collapse-item-header mdui-list-item mdui-ripple">
          <i class="
                    mdui-list-item-icon
                    mdui-icon
                    material-icons
                    mdui-text-color-deep-orange">layers</i>
          <div class="mdui-list-item-content">API请求</div>
          <i class="mdui-collapse-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
        </div>
        <div class="mdui-collapse-item-body mdui-list">
          <a href="/release/API/color" class="
                          mdui-list-item
                          mdui-ripple
                          ">颜色与主题</a><a href="/release/API/font" class="
                          mdui-list-item
                          mdui-ripple
                          ">字体</a>
        </div>
      </div>
      <div class="
                mdui-collapse-item
                ">
        <div class="mdui-collapse-item-header mdui-list-item mdui-ripple">
          <i class="
                    mdui-list-item-icon
                    mdui-icon
                    material-icons
                    mdui-text-color-green">widgets</i>
          <div class="mdui-list-item-content">可视化请求</div>
          <i class="mdui-collapse-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
        </div>
        <div class="mdui-collapse-item-body mdui-list">
          <a href="/release/API/search" class="
                          mdui-list-item
                          mdui-ripple
                          ">搜索</a><a href="/release/API/button" class="
                          mdui-list-item
                          mdui-ripple
                          ">按钮</a>
        </div>
      </div>
      <div class="
                mdui-collapse-item
                ">
        <div class="mdui-collapse-item-header mdui-list-item mdui-ripple">
          <i class="
                    mdui-list-item-icon
                    mdui-icon
                    material-icons
                    mdui-text-color-brown">view_carousel</i>
          <div class="mdui-list-item-content">其他</div>
          <i class="mdui-collapse-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
        </div>
        <div class="mdui-collapse-item-body mdui-list">
          <a href="/release/API/collapse" class="
                          mdui-list-item
                          mdui-ripple
                          ">Collapse</a><a href="/release/API/headroom" class="
                          mdui-list-item
                          mdui-ripple
                          ">Headroom</a>
        </div>
      </div>
      <div class="
                mdui-collapse-item
                ">
        <div class="mdui-collapse-item-header mdui-list-item mdui-ripple">
          <i class="
                    mdui-list-item-icon
                    mdui-icon
                    material-icons
                    mdui-text-color-grey">settings</i>
          <div class="mdui-list-item-content">设置</div>
          <i class="mdui-collapse-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
        </div>
        <div class="mdui-collapse-item-body mdui-list">
          <a href="/release/API/token" class="
                          mdui-list-item
                          mdui-ripple
                          ">Token</a><a href="/release/API/preview" class="
                          mdui-list-item
                          mdui-ripple
                          ">预览设置</a>
        </div>
      </div>
    </div>
  </div>
    <a id="anchor-top"></a>'''
title = '''
    <div class="container p-index mdui-container">
        <h1 class="title mdui-text-color-theme">{}</h1>
        <div class="chapter">
            <div class="mdui-typo">
'''

get_part = '''<div class="mdui-col-md-3 mdui-col-sm-8 ">
            <a class="mdui-btn mdui-ripple mdui-btn-raised mdui-btn-block mdui-color-theme-accent" id="get_id_dir"><div class="mdui-progress-indeterminate"></div></a>
            <br>
            <br>
          </div>
        <script>
          function getQueryString(name) {
            let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
            let r = window.location.search.substr(1).match(reg);
            if (r != null) {
              return decodeURIComponent(r[2]);
            };
            return null;
          }
          window.onload = function () {
            var id = getQueryString('id');
            var skiptoken = getQueryString('skiptoken');
            var t = document.getElementById("get_id_dir");
            if (skiptoken == null){ var fix = ""; }else{ var fix = "&skiptoken=" + skiptoken; };
            if (id != null & id != "") {
              if (document.location.search.includes("thumbnails")) {
                t.href = document.location.origin + document.location.pathname + '?id=' + id + fix;
                t.innerText = "查看具体内容";
              }
              else {
                t.href = document.location.origin + document.location.pathname + '?id=' + id + "&thumbnails" + fix;
                t.innerText = "查看缩略图";
              }

            } else {
              t.hidden = true
            }
          }         
        </script>'''

part = "        <p>{}</p>"

base2 = '''</div>



            <div class="mdui-typo">
      <h4 class="article-title">开始使用</h4>
    </div>
    <div class="mdui-row-xs-1 mdui-row-sm-2 mdui-row-md-3 mdui-row-lg-4">
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/introduction" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">简介</a>
      </div>
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/download" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">下载</a>
      </div>
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/compatibility" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">兼容性</a>
      </div>
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/jq" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">JavaScript
          工具库</a>
      </div>
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/global" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">JavaScript
          全局方法</a>
      </div>
    </div>
    <div class="mdui-typo">
      <h4 class="article-title">API请求</h4>
    </div>
    <div class="mdui-row-xs-1 mdui-row-sm-2 mdui-row-md-3 mdui-row-lg-4">
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/color" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">颜色与主题</a>
      </div>
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/font" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">字体</a>
      </div>
    </div>
    <div class="mdui-typo">
      <h4 class="article-title">可视化请求</h4>
    </div>
    <div class="mdui-row-xs-1 mdui-row-sm-2 mdui-row-md-3 mdui-row-lg-4">
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/search" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">搜索</a>
      </div>
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/button" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">按钮</a>
      </div>
    </div>
    <div class="mdui-typo">
      <h4 class="article-title">其他</h4>
    </div>
    <div class="mdui-row-xs-1 mdui-row-sm-2 mdui-row-md-3 mdui-row-lg-4">
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/collapse" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">Collapse</a>
      </div>
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/headroom" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">Headroom</a>
      </div>
    </div>
    <div class="mdui-typo">
      <h4 class="article-title">设置</h4>
    </div>
    <div class="mdui-row-xs-1 mdui-row-sm-2 mdui-row-md-3 mdui-row-lg-4">
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/token" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">Token设置</a>
      </div>
      <div class="mdui-col mdui-m-b-1">
        <a href="/release/API/preview" class="mdui-btn mdui-btn-block mdui-text-left mdui-ripple">预览设置</a>
      </div>
    </div>

            <div class="mdui-typo">
                <h4 class="article-title">相关链接</h4>
                <p><label>幻海实验室 官网：<a href="//app.phantom-sea-limited.ltd"
                            target="_blank">phantom-sea-limited.ltd</a></label></p>
            </div>
        </div>

<script>
          function copy(data) {
            let input = document.createElement("input"); // 直接构建input
            input.setAttribute("readonly", "readonly"); //设置只读，否则移动端会有键盘弹出
            input.value = data; // 设置内容
            document.body.appendChild(input); // 添加临时实例
            input.select(); // 选择实例内容
            document.execCommand("Copy"); // 执行复制
            document.body.removeChild(input); // 删除临时实例
            // this.$message.success("复制成功");
          }
          function copy_link(type) {
            if (type == 1) {
              var urlbase = 'https://service-90zr9afj-1258642780.sh.apigw.tencentcs.com';
              url = urlbase + location.pathname + location.search;
              url = urlbase + '/release/API/share?token=' + getCookie('token') + '&url=' + url;
            };
            if (type == 2) {
              var urlbase = 'https://service-90zr9afj-1258642780.sh.apigw.tencentcs.com';
              if (location.search == '') { url = urlbase + location.pathname + '?share=' + getCookie('token'); }
              else { url = urlbase + location.pathname + location.search + '&share=' + getCookie('token'); }
            };
            if (type == 3) {
              var urlbase = 'https://api-cdn.phantom-sea-limited.ltd';
              url = urlbase + location.pathname + location.search;
              url = urlbase + '/release/API/share?token=' + getCookie('token') + '&url=' + url;
            };
            if (type == 4) {
              var urlbase = 'https://api-cdn.phantom-sea-limited.ltd';
              if (location.search == '') { url = urlbase + location.pathname + '?share=' + getCookie('token'); }
              else { url = urlbase + location.pathname + location.search + '&share=' + getCookie('token'); }
            };
            copy(url);
            mdui.alert('复制成功');
          }
        </script>
        <button class="mdui-fab mdui-fab-fixed" mdui-dialog="{target: '#share'}"><i
            class="mdui-icon material-icons">share</i></button>
        <div class="mdui-dialog" id="share">
          <div class="mdui-tab mdui-tab-full-width" id="share-tab">
            <a href="#share-tab1" class="mdui-ripple">分享到QQ</a>
            <a href="#share-tab2" class="mdui-ripple">分享到其他</a>
          </div>
          <div id="share-tab1" class="mdui-p-a-2">
            <div class="mdui-typo-title-opacity">能够直接在QQ或微信直接打开的链接</div>
            <p>*链接较长，有效时间到当天0点为止</p>
            <p>*分享链接的生成基于您本地的token，如果权限不正常或无权限，生成的分享链接也无权限</p>
            <div class="mdui-typo-title-opacity">无限制链接
              <button class="mdui-btn  mdui-btn-dense mdui-color-theme-accent mdui-ripple" onclick="copy_link(1)"
                mdui-dialog-close>点击复制
                <i class="mdui-icon material-icons">content_copy</i></button>
            </div>
            <p>*得到链接的人<mark>可以</mark>访问其他内容</p>
            <div class="mdui-typo-title-opacity">有限制链接
              <button class="mdui-btn  mdui-btn-dense mdui-color-theme-accent mdui-ripple" onclick="copy_link(2)"
                mdui-dialog-close>点击复制
                <i class="mdui-icon material-icons">content_copy</i></button>
            </div>
            <p>*得到链接的人<mark>只能</mark>访问该链接</p>
          </div>
          <div id="share-tab2" class="mdui-p-a-2">
            <div class="mdui-typo-title-opacity">正常链接</div>
            <p>*链接长度正常，有效时间到当天0点为止</p>
            <p>*分享链接的生成基于您本地的token，如果权限不正常或无权限，生成的分享链接也无权限</p>
            <div class="mdui-typo-title-opacity">无限制链接
              <button class="mdui-btn  mdui-btn-dense mdui-color-theme-accent mdui-ripple" onclick="copy_link(3)"
                mdui-dialog-close>点击复制
                <i class="mdui-icon material-icons">content_copy</i></button>
            </div>
            <p>*得到链接的人<mark>可以</mark>访问其他内容</p>
            <div class="mdui-typo-title-opacity">有限制链接
              <button class="mdui-btn  mdui-btn-dense mdui-color-theme-accent mdui-ripple" onclick="copy_link(4)"
                mdui-dialog-close>点击复制
                <i class="mdui-icon material-icons">content_copy</i></button>
            </div>
            <p>*得到链接的人<mark>只能</mark>访问该链接</p>
          </div>
        </div>

        <script>
          var $ = mdui.$;
          var tab = new mdui.Tab('#share-tab');
          $('#share').on('open.mdui.dialog', function () {
            tab.handleUpdate();
          });
        </script>


    <div class="footer-nav mdui-color-theme">
        <div class="mdui-container">
            <div class="mdui-row">

                <div class="mdui-col-xs-2 mdui-col-sm-6 footer-nav-left"></div>

                <a href="//app.phantom-sea-limited.ltd"
                    class="mdui-ripple mdui-color-theme mdui-col-xs-10 mdui-col-sm-6 footer-nav-right">
                    <div class="footer-nav-text">
                        <i class="mdui-icon material-icons">arrow_forward</i>
                        <span class="footer-nav-direction">© 2019-2022</span>
                        <div class="footer-nav-chapter">幻海实验室</div>
                    </div>
                </a>
            </div>
        </div>
    </div>
</body>

</html>
'''

setu= '''
<script>
      function post_command() {
        var t = document.getElementById("setu");
        var t2 = document.getElementById("setuIN");
        url = "/release/PIXIV/tag?tag=" + t.value + "&random";
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
          if (xhr.readyState == 4 && xhr.status == 200) {
            a = eval('(' + xhr.responseText + ')');
            var tmp = document.createElement("img");
            tmp.src = a["urls"]["original"];
            t2.innerHTML = "";
            t2.appendChild(tmp);
          }
          if (xhr.status == 430) {
            t2.innerText = "出错了喵";
          }
        }
        xhr.open('GET', url , true);
        xhr.send();
        t2.innerHTML = '<div class="mdui-progress"><div class="mdui-progress-indeterminate"></div></div>';
        return false;
      }
    </script>
    <form>
      <div class="mdui-textfield">
        <div class="mdui-col-xs-6">
          <input class="mdui-textfield-input" type="text" placeholder="涩图TAG" required="" id="setu" onkeydown="if(event.keyCode==13){return post_command();}">
          <div class="mdui-textfield-error"></div>
        </div>
        <div class="mdui-col-xs-3">
          <button class="mdui-btn" onclick="return post_command()" id="search">冲!</button>
        </div>
      </div>
    </form>
    <div id="setuIN"></div>'''


def SETU():
    return base + title.format("涩图") + setu + base2