from lxml import etree
import gzip
import webapp2_extras
import base64
import datetime

myxml = """
<article lang="">
  <para><note><remark>saved from url=(0090)https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers</remark></note>window.mod_pagespeed_start = Number(new Date());//&lt;![CDATA[
(function(){function d(b){var a=window;if(a.addEventListener)a.addEventListener("load",b,!1);else if(a.attachEvent)a.attachEvent("onload",b);else{var c=a.onload;a.onload=function(){b.call(this);c&amp;&amp;c.call(this)}}}var p=Date.now||function(){return+new Date};window.pagespeed=window.pagespeed||{};var q=window.pagespeed;function r(){this.a=!0}r.prototype.c=function(b){b=parseInt(b.substring(0,b.indexOf(" ")),10);return!isNaN(b)&amp;&amp;b&lt;=p()};r.prototype.hasExpired=r.prototype.c;r.prototype.b=function(b){return b.substring(b.indexOf(" ",b.indexOf(" ")+1)+1)};r.prototype.getData=r.prototype.b;r.prototype.f=function(b){var a=document.getElementsByTagName("script"),a=a[a.length-1];a.parentNode.replaceChild(b,a)};r.prototype.replaceLastScript=r.prototype.f;
r.prototype.g=function(b){var a=window.localStorage.getItem("pagespeed_lsc_url:"+b),c=document.createElement(a?"style":"link");a&amp;&amp;!this.c(a)?(c.type="text/css",c.appendChild(document.createTextNode(this.b(a)))):(c.rel="stylesheet",c.href=b,this.a=!0);this.f(c)};r.prototype.inlineCss=r.prototype.g;
r.prototype.h=function(b,a){var c=window.localStorage.getItem("pagespeed_lsc_url:"+b+" pagespeed_lsc_hash:"+a),f=document.createElement("img");c&amp;&amp;!this.c(c)?f.src=this.b(c):(f.src=b,this.a=!0);for(var c=2,k=arguments.length;c&lt;k;++c){var g=arguments[c].indexOf("=");f.setAttribute(arguments[c].substring(0,g),arguments[c].substring(g+1))}this.f(f)};r.prototype.inlineImg=r.prototype.h;
function t(b,a,c,f){a=document.getElementsByTagName(a);for(var k=0,g=a.length;k&lt;g;++k){var e=a[k],m=e.getAttribute("data-pagespeed-lsc-hash"),h=e.getAttribute("data-pagespeed-lsc-url");if(m&amp;&amp;h){h="pagespeed_lsc_url:"+h;c&amp;&amp;(h+=" pagespeed_lsc_hash:"+m);var l=e.getAttribute("data-pagespeed-lsc-expiry"),l=l?(new Date(l)).getTime():"",e=f(e);if(!e){var n=window.localStorage.getItem(h);n&amp;&amp;(e=b.b(n))}e&amp;&amp;(window.localStorage.setItem(h,l+" "+m+" "+e),b.a=!0)}}}
function u(b){t(b,"img",!0,function(a){return a.src});t(b,"style",!1,function(a){return a.firstChild?a.firstChild.nodeValue:null})}
q.i=function(){if(window.localStorage){var b=new r;q.localStorageCache=b;d(function(){u(b)});d(function(){if(b.a){for(var a=[],c=[],f=0,k=p(),g=0,e=window.localStorage.length;g&lt;e;++g){var m=window.localStorage.key(g);if(!m.indexOf("pagespeed_lsc_url:")){var h=window.localStorage.getItem(m),l=h.indexOf(" "),n=parseInt(h.substring(0,l),10);if(!isNaN(n))if(n&lt;=k){a.push(m);continue}else if(n&lt;f||0==f)f=n;c.push(h.substring(l+1,h.indexOf(" ",l+1)))}}k="";f&amp;&amp;(k="; expires="+(new Date(f)).toUTCString());
document.cookie="_GPSLSC="+c.join("!")+k;g=0;for(e=a.length;g&lt;e;++g)window.localStorage.removeItem(a[g]);b.a=!1}})}};q.localStorageCacheInit=q.i;})();
pagespeed.localStorageCacheInit();
//]]&gt;<note><remark>&lt;!--[if lte IE 8]&gt;</remark></note><note><remark>&lt;script src="/core/assets/vendor/html5shiv/html5shiv.min.js?v=3.7.3"&gt;&lt;/script&gt;</remark></note><note><remark>&lt;![endif]--&gt;</remark></note>//&lt;![CDATA[
(function(){window.pagespeed=window.pagespeed||{};var f=window.pagespeed;function h(e,a,c,b){this.f=e;this.a=a;this.b=c;this.g=b}f.beaconUrl="";
function k(e){var a=e.f,c=window.mod_pagespeed_start,b=Number(new Date)-c,a=a+(-1==a.indexOf("?")?"?":"&amp;"),a=a+"ets="+("load"==e.a?"load:":"unload:"),a=a+b;if("beforeunload"!=e.a||!window.mod_pagespeed_loaded){a+="&amp;r"+e.a+"=";if(window.performance){var b=window.performance.timing,d=b.navigationStart,g=b.requestStart,a=a+(b[e.a+"EventStart"]-d),a=a+("&amp;nav="+(b.fetchStart-d)),a=a+("&amp;dns="+(b.domainLookupEnd-b.domainLookupStart)),a=a+("&amp;connect="+(b.connectEnd-b.connectStart)),a=a+("&amp;req_start="+(g-
d)),a=a+("&amp;ttfb="+(b.responseStart-g)),a=a+("&amp;dwld="+(b.responseEnd-b.responseStart)),a=a+("&amp;dom_c="+(b.domContentLoadedEventStart-d));window.performance.navigation&amp;&amp;(a+="&amp;nt="+window.performance.navigation.type);d=-1;b.msFirstPaint?d=b.msFirstPaint:window.chrome&amp;&amp;window.chrome.loadTimes&amp;&amp;(d=Math.floor(1E3*window.chrome.loadTimes().firstPaintTime));d=d-g;0&lt;=d&amp;&amp;(a+="&amp;fp="+d)}else a+=b;f.getResourceTimingData&amp;&amp;window.parent==window&amp;&amp;(a+=f.getResourceTimingData());a+=window.parent!=window?"&amp;ifr=1":"&amp;ifr=0";
"load"==e.a&amp;&amp;(window.mod_pagespeed_loaded=!0,(b=window.mod_pagespeed_num_resources_prefetched)&amp;&amp;(a+="&amp;nrp="+b),(b=window.mod_pagespeed_prefetch_start)&amp;&amp;(a+="&amp;htmlAt="+(c-b)));f.panelLoader&amp;&amp;(c=f.panelLoader.getCsiTimingsString(),""!=c&amp;&amp;(a+="&amp;b_csi="+c));f.criticalCss&amp;&amp;(c=f.criticalCss,a+="&amp;ccis="+c.total_critical_inlined_size+"&amp;cces="+c.total_original_external_size+"&amp;ccos="+c.total_overhead_size+"&amp;ccrl="+c.num_replaced_links+"&amp;ccul="+c.num_unreplaced_links);a+="&amp;dpr="+window.devicePixelRatio;""!=
e.b&amp;&amp;(a+=e.b);document.referrer&amp;&amp;(a+="&amp;ref="+encodeURIComponent(document.referrer));a+="&amp;url="+encodeURIComponent(e.g);f.beaconUrl=a;(new Image).src=a}}f.c=function(e,a,c,b){var d=new h(e,a,c,b);window.addEventListener?window.addEventListener(a,function(){k(d)},!1):window.attachEvent("on"+a,function(){k(d)})};f.addInstrumentationInit=f.c;})();

pagespeed.addInstrumentationInit('/mod_pagespeed_beacon', 'beforeunload', '', 'https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers');
//]]&gt;<note><remark>HTML: &lt;noscript&gt;</remark></note>Please click <ulink url="https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers?PageSpeed=noscript">here</ulink> if you are not redirected within a few seconds.</para>
  <para><note><remark>HTML: &lt;/noscript&gt;</remark></note><ulink url="https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers#main-content">Skip to main content</ulink><ulink url="https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers#main-content"><note><remark>HTML: &lt;noscript aria-hidden="true"&gt;</remark></note></ulink><ulink url="https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers#main-content"> </ulink><note><remark>HTML: &lt;/noscript&gt;</remark></note> </para>
  <orderedlist>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/">Home</ulink> </para>
    </listitem>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/services">Services</ulink> </para>
    </listitem>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/efficiency-and-savings">Efficiency and savings</ulink> </para>
    </listitem>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/safety">Safety</ulink> </para>
    </listitem>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/community">Community</ulink> </para>
    </listitem>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/ourcompany">Our company</ulink> </para>
    </listitem>
  </orderedlist>
  <orderedlist>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/billing-payments">Billing and payments</ulink> </para>
    </listitem>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/outages">Outage center</ulink> </para>
    </listitem>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/app-startstop">Start/stop/move service</ulink> </para>
    </listitem>
    <listitem>
      <para><ulink url="https://www.blackhillsenergy.com/customer-service">Customer service</ulink> </para>
    </listitem>
  </orderedlist>
  <para><ulink url="https://www.blackhillsenergy.com/my-account">Log In</ulink> </para>
  <para>location_on </para>
  <para>Enter your ZIP Code </para>
  <para><ulink url="https://www.blackhillsenergy.com/my-account/#/dashboard">Log In</ulink> <ulink url="https://www.blackhillsenergy.com/outages">Outages</ulink> <ulink url="https://www.blackhillsenergy.com/customer-service">Customer Service</ulink> </para>
  <para>menu </para>
  <para>search </para>
  <para><anchor id="search-field"/> search close </para>
  <para>Please enter the ZIP code of your service area so we can provide the most relevant information for you. </para>
  <para>location_on <anchor id="zip-search--field"/> </para>
  <para>  </para>
  <para><ulink url="https://www.blackhillsenergy.com/">Home</ulink><ulink url="https://www.blackhillsenergy.com/services">Services</ulink><ulink url="https://www.blackhillsenergy.com/services/choice-gas-program">Choice Gas program</ulink> </para>
  <sect1 id="block-bhe-content">
    <para>Nebraska Choice Gas customers </para>
    <para>//&lt;![CDATA[
(function(){var g=this;function h(b,d){var a=b.split("."),c=g;a[0]in c||!c.execScript||c.execScript("var "+a[0]);for(var e;a.length&amp;&amp;(e=a.shift());)a.length||void 0===d?c[e]?c=c[e]:c=c[e]={}:c[e]=d};function l(b){var d=b.length;if(0&lt;d){for(var a=Array(d),c=0;c&lt;d;c++)a[c]=b[c];return a}return[]};function m(b){var d=window;if(d.addEventListener)d.addEventListener("load",b,!1);else if(d.attachEvent)d.attachEvent("onload",b);else{var a=d.onload;d.onload=function(){b.call(this);a&amp;&amp;a.call(this)}}};var n;function p(b,d,a,c,e){this.h=b;this.j=d;this.l=a;this.f=e;this.g={height:window.innerHeight||document.documentElement.clientHeight||document.body.clientHeight,width:window.innerWidth||document.documentElement.clientWidth||document.body.clientWidth};this.i=c;this.b={};this.a=[];this.c={}}function q(b,d){var a,c,e=d.getAttribute("data-pagespeed-url-hash");if(a=e&amp;&amp;!(e in b.c))if(0&gt;=d.offsetWidth&amp;&amp;0&gt;=d.offsetHeight)a=!1;else{c=d.getBoundingClientRect();var f=document.body;a=c.top+("pageYOffset"in window?window.pageYOffset:(document.documentElement||f.parentNode||f).scrollTop);c=c.left+("pageXOffset"in window?window.pageXOffset:(document.documentElement||f.parentNode||f).scrollLeft);f=a.toString()+","+c;b.b.hasOwnProperty(f)?a=!1:(b.b[f]=!0,a=a&lt;=b.g.height&amp;&amp;c&lt;=b.g.width)}a&amp;&amp;(b.a.push(e),b.c[e]=!0)}p.prototype.checkImageForCriticality=function(b){b.getBoundingClientRect&amp;&amp;q(this,b)};h("pagespeed.CriticalImages.checkImageForCriticality",function(b){n.checkImageForCriticality(b)});h("pagespeed.CriticalImages.checkCriticalImages",function(){r(n)});function r(b){b.b={};for(var d=["IMG","INPUT"],a=[],c=0;c&lt;d.length;++c)a=a.concat(l(document.getElementsByTagName(d[c])));if(0!=a.length&amp;&amp;a[0].getBoundingClientRect){for(c=0;d=a[c];++c)q(b,d);a="test="+b.l;b.f&amp;&amp;(a+="&amp;n="+b.f);if(d=0!=b.a.length)for(a+="&amp;ci="+encodeURIComponent(b.a[0]),c=1;c&lt;b.a.length;++c){var e=","+encodeURIComponent(b.a[c]);131072&gt;=a.length+e.length&amp;&amp;(a+=e)}b.i&amp;&amp;(e="&amp;rd="+encodeURIComponent(JSON.stringify(t())),131072&gt;=a.length+e.length&amp;&amp;(a+=e),d=!0);u=a;if(d){c=b.h;b=b.j;var f;if(window.XMLHttpRequest)f=new XMLHttpRequest;else if(window.ActiveXObject)try{f=new ActiveXObject("Msxml2.XMLHTTP")}catch(k){try{f=new ActiveXObject("Microsoft.XMLHTTP")}catch(v){}}f&amp;&amp;(f.open("POST",c+(-1==c.indexOf("?")?"?":"&amp;")+"url="+encodeURIComponent(b)),f.setRequestHeader("Content-Type","application/x-www-form-urlencoded"),f.send(a))}}}function t(){var b={},d=document.getElementsByTagName("IMG");if(0==d.length)return{};var a=d[0];if(!("naturalWidth"in a&amp;&amp;"naturalHeight"in a))return{};for(var c=0;a=d[c];++c){var e=a.getAttribute("data-pagespeed-url-hash");e&amp;&amp;(!(e in b)&amp;&amp;0&lt;a.width&amp;&amp;0&lt;a.height&amp;&amp;0&lt;a.naturalWidth&amp;&amp;0&lt;a.naturalHeight||e in b&amp;&amp;a.width&gt;=b[e].o&amp;&amp;a.height&gt;=b[e].m)&amp;&amp;(b[e]={rw:a.width,rh:a.height,ow:a.naturalWidth,test:a.naturalHeight})}return b}var u="";h("pagespeed.CriticalImages.getBeaconData",function(){return u});h("pagespeed.CriticalImages.Run",function(b,d,a,c,e,f){var k=new p(b,d,a,e,f);n=k;c&amp;&amp;m(function(){window.setTimeout(function(){r(k)},0)})});})();pagespeed.CriticalImages.Run('/mod_pagespeed_beacon','https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers','8Exh60Qgd3',true,false,'IntkKjrFIdE');
//]]&gt;<inlinegraphic fileref="./Nebraska%20Choice%20Gas%20customers%20_%20Black%20Hills%20Energy_files/choice_gas_ne.jpg" width="9.2811inch" depth="6.3335inch"/> </para>
    <para>
      <ulink url="https://www.blackhillsenergy.com/app-choicegas/">Sign Up for Choice Gas</ulink>
    </para>
    <para>The Choice Gas Program gives you the opportunity to choose your natural gas provider and the pricing options that best suit your needs.</para>
    <para>The selection period for our 2020 Nebraska Choice Gas Program begins April 10, 2020, and ends April 23, 2020, at midnight CDT.</para>
    <title>How it works</title>
    <para>No matter which supplier you select, we will maintain your local natural gas system, read the meters, send bills and answer any questions you have.</para>
    <para>If you don’t choose a supplier, your account will roll over to your current supplier and pricing option. If you roll over, your final rate will be determined within 15 days after the selection period ends.</para>
    <para>The natural gas commodity price that you will be charged will not carry over from the previous year unless the supplier agrees to do so. Your final rollover price may be different from the prices quoted during the selection period.</para>
    <title>Multi-year selection option</title>
    <para>If you select a multi-year term through your supplier, you’ll know your price option and rate —not only for the new program year (June-May) — but for future program years as well. When you select a multi-year term, during the term of your selection, you will not:</para>
    <orderedlist>
      <listitem>
        <para>Receive an annual selection packet </para>
      </listitem>
      <listitem>
        <para>Receive supplier marketing contact </para>
      </listitem>
      <listitem>
        <para>Be eligible to make another selection </para>
      </listitem>
    </orderedlist>
    <para>All Choice Gas selections are specific to your current service address and are nontransferable. Multi-year selection options are customer and service address specific. So, if you move during the term of a multi-year selection, you will be eligible to make a selection at your new service address during the next annual Choice Gas selection period.</para>
    <para>For more information about multi-year options, contact any of the Choice Gas participating suppliers.</para>
    <title>Customer letter</title>
    <para>
      <ulink url="https://www.blackhillsenergy.com/sites/blackhillsenergy.com/files/choicegas_ne_letter_0.pdf">Download the 2020 Nebraska Choice Gas customer letter.</ulink>
    </para>
    <title>Guide book</title>
    <para><ulink url="https://www.blackhillsenergy.com/sites/blackhillsenergy.com/files/choicegas_ne_guidebook.pdf">Download the 2020 Nebraska Choice Gas guide book</ulink>.</para>
    <title>Sign up</title>
    <para>Between April 10-23, there are four ways to make your selection:</para>
    <orderedlist>
      <listitem>
        <para><ulink url="https://www.blackhillsenergy.com/app-choicegas/">Online</ulink> </para>
      </listitem>
      <listitem>
        <para>Supplier submission </para>
      </listitem>
      <listitem>
        <para>Mail using the selection form(s) mailed to you  </para>
      </listitem>
      <listitem>
        <para>Automatic rollover </para>
      </listitem>
    </orderedlist>
    <para>You will need your account number, control number and the confirmation code for the supplier you desire to choose for the 2019-20 program year.</para>
    <para>If you have multiple accounts, you must submit separate selections for each account.</para>
    <title>2020 Nebraska Choice Gas supplier selection results</title>
    <para>Results updated 05/07/2020</para>
    <informaltable frame="all">
      <tgroup cols="2"><thead><row><entry><para>Supplier</para></entry><entry><para>Number of Enrollees</para></entry></row></thead><tbody><row><entry><para><ulink url="http://www.aceenergy.org/">ACE</ulink> (Public Alliance for Community Energy)800-454-4759(se habla espanol)</para></entry><entry><para>14083</para></entry></row><row><entry><para><ulink url="https://www.unclefrankenergy.com/">Uncle Frank Energy Services</ulink>833-372-6564 (833-Frank NG)</para></entry><entry><para>1361</para></entry></row><row><entry><para><ulink url="http://www.vistaenergymarketing.com/">Vista Energy Marketing</ulink>888-508-4782(se habla espanol)</para></entry><entry><para>10292</para></entry></row><row><entry><para><ulink url="http://www.nebraskagas.com/">Constellation Energy</ulink>877-274-5710</para></entry><entry><para>12514</para></entry></row><row><entry><para><ulink url="https://trustbhes.com/">Black Hills Energy Services</ulink>800-215-3035(se habla espanol)</para></entry><entry><para>29032</para></entry></row><row><entry><para><ulink url="http://www.betternegas.com/">CenterPoint Energy Services, Inc.</ulink>888-200-3788(se habla espanol)</para></entry><entry><para>9688</para></entry></row><row><entry><para><ulink url="http://www.woodriverenergy.com/">WoodRiver Energy, LLC</ulink>888-510-9315</para></entry><entry><para>2398</para></entry></row></tbody></tgroup>
    </informaltable>
    <title>Supplier marketing and customer contact information</title>
    <para>The natural gas market can be volatile, with available rates changing frequently during the selection period. To give you timely information so you can make the Choice Gas selection that best suits your needs, participating suppliers may contact you by phone, text or email to share their individual offerings. We provide all suppliers with the phone number and email address you may have provided for your Black Hills Energy account.Supplier marketing and customer contact information</para>
    <para>Although we want you to have the chance to receive this additional information from the suppliers, we also understand that calls, texts and emails may be burdensome. Each supplier is limited as to how often they can contact you. If you no longer want to receive these communications from a supplier, request to be removed from their call list or opt out of email communications. After you’ve completed a successful selection, you shouldn’t receive any further contact from suppliers.</para>
    <title>Contact us</title>
    <para>For more information about Choice Gas, contact us at <ulink url="tel://8772453506">877-245-3506</ulink>. We are available according to the times and dates listed below.</para>
    <informaltable frame="all">
      <tgroup cols="2"><tbody><row><entry><para>April 10</para></entry><entry><para>8 a.m. – 7:30 p.m. CDT</para></entry></row><row><entry><para>April 13 - April 17</para></entry><entry><para>8 a.m. – 7:30 p.m. CDT</para></entry></row><row><entry><para>April 20 - April 23</para></entry><entry><para>8 a.m. – 7:30 p.m. CDT </para></entry></row></tbody></tgroup>
    </informaltable>
    <title>Frequently asked questions</title>
    <sect2 id="accordion-3293">
      <para/>
      <sect3 id="heading-accordion-3293-1">
        <title>Where can I get more information about the 2019-2020 Choice Gas Program and suppliers?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-1">
        <orderedlist>
          <listitem>
            <para><ulink url="https://www.blackhillsenergy.com/sites/blackhillsenergy.com/files/choicegas_ne_guidebook.pdf">Download the guidebook</ulink>. </para>
          </listitem>
          <listitem>
            <para><ulink url="https://www.blackhillsenergy.com/node/362">Click here for more information about the suppliers and their pricing options.</ulink> </para>
          </listitem>
        </orderedlist>
      </sect3>
      <sect3 id="heading-accordion-3293-2">
        <title>How do I select my supplier?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-2">
        <para>You can automatically roll over to your current supplier and pricing option or submit a selection online, through your chosen supplier or by mail.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-3">
        <title>What constitutes a “valid” selection?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-3">
        <para>A selection is considered valid when you submit your choice through one of the accepted submission methods on or before Thursday, April 25, 2019. Confirmation codes are time-sensitive, so check with your supplier about your codes’ expiration date. The first valid selection Black Hills Gas Distribution, LLC receives will be considered your final choice. Record your verification number if you’re submitting your selection online. You’ll need to sign any mailed selection forms for them to be valid.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-4">
        <title>What happens if I move during the Choice Gas program year?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-4">
        <para>If you move from one service address to another, or a new customer moves to a service address within the Choice Gas Program territory, that customer will continue with the supplier previously selected for that address. New construction customers will be mailed a selection packet. For additional questions about service address issues, call 888-890-5554.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-5">
        <title>Does the Choice Gas Program affect the quality of distribution service?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-5">
        <para>No. Regardless of your selection, Black Hills Gas Distribution, LLC will continue to provide meter reading and billing services, respond to gas leaks, and ensure the safety and reliability of the gas supply to Choice Gas Program communities.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-6">
        <title>Does the Choice Gas Program affect distribution charges?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-6">
        <para>No. Changes in distribution rates occur from time to time and are subject to Nebraska Public Service Commission approval.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-7">
        <title>Are the suppliers reliable?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-7">
        <para>Yes. Participating suppliers must meet requirements in Black Hills Gas Distribution, LLC's tariff and approved by the Nebraska Public Service Commission.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-8">
        <title>What if I’m on Budget Billing?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-8">
        <para>If you’re a Budget Billing customer and select a fixed monthly bill price option a supplier offers, your outstanding Budget Billing balance will be due in full with your June billing.</para>
      </sect3>
    </sect2>
  </sect1>
  <sect1>
    <title>How it works</title>
    <para>No matter which supplier you select, we will maintain your local natural gas system, read the meters, send bills and answer any questions you have.</para>
    <para>If you don’t choose a supplier, your account will roll over to your current supplier and pricing option. If you roll over, your final rate will be determined within 15 days after the selection period ends.</para>
    <para>The natural gas commodity price that you will be charged will not carry over from the previous year unless the supplier agrees to do so. Your final rollover price may be different from the prices quoted during the selection period.</para>
  </sect1>
  <sect1>
    <title>Multi-year selection option</title>
    <para>If you select a multi-year term through your supplier, you’ll know your price option and rate —not only for the new program year (June-May) — but for future program years as well. When you select a multi-year term, during the term of your selection, you will not:</para>
    <orderedlist>
      <listitem>
        <para>Receive an annual selection packet </para>
      </listitem>
      <listitem>
        <para>Receive supplier marketing contact </para>
      </listitem>
      <listitem>
        <para>Be eligible to make another selection </para>
      </listitem>
    </orderedlist>
    <para>All Choice Gas selections are specific to your current service address and are nontransferable. Multi-year selection options are customer and service address specific. So, if you move during the term of a multi-year selection, you will be eligible to make a selection at your new service address during the next annual Choice Gas selection period.</para>
    <para>For more information about multi-year options, contact any of the Choice Gas participating suppliers.</para>
  </sect1>
  <sect1>
    <title>Customer letter</title>
    <para>
      <ulink url="https://www.blackhillsenergy.com/sites/blackhillsenergy.com/files/choicegas_ne_letter_0.pdf">Download the 2020 Nebraska Choice Gas customer letter.</ulink>
    </para>
  </sect1>
  <sect1>
    <title>Guide book</title>
    <para><ulink url="https://www.blackhillsenergy.com/sites/blackhillsenergy.com/files/choicegas_ne_guidebook.pdf">Download the 2020 Nebraska Choice Gas guide book</ulink>.</para>
  </sect1>
  <sect1>
    <title>Sign up</title>
    <para>Between April 10-23, there are four ways to make your selection:</para>
    <orderedlist>
      <listitem>
        <para><ulink url="https://www.blackhillsenergy.com/app-choicegas/">Online</ulink> </para>
      </listitem>
      <listitem>
        <para>Supplier submission </para>
      </listitem>
      <listitem>
        <para>Mail using the selection form(s) mailed to you  </para>
      </listitem>
      <listitem>
        <para>Automatic rollover </para>
      </listitem>
    </orderedlist>
    <para>You will need your account number, control number and the confirmation code for the supplier you desire to choose for the 2019-20 program year.</para>
    <para>If you have multiple accounts, you must submit separate selections for each account.</para>
  </sect1>
  <sect1>
    <title>2020 Nebraska Choice Gas supplier selection results</title>
    <para>Results updated 05/07/2020</para>
    <informaltable frame="all">
      <tgroup cols="2"><thead><row><entry><para>Supplier</para></entry><entry><para>Number of Enrollees</para></entry></row></thead><tbody><row><entry><para><ulink url="http://www.aceenergy.org/">ACE</ulink> (Public Alliance for Community Energy)800-454-4759(se habla espanol)</para></entry><entry><para>14083</para></entry></row><row><entry><para><ulink url="https://www.unclefrankenergy.com/">Uncle Frank Energy Services</ulink>833-372-6564 (833-Frank NG)</para></entry><entry><para>1361</para></entry></row><row><entry><para><ulink url="http://www.vistaenergymarketing.com/">Vista Energy Marketing</ulink>888-508-4782(se habla espanol)</para></entry><entry><para>10292</para></entry></row><row><entry><para><ulink url="http://www.nebraskagas.com/">Constellation Energy</ulink>877-274-5710</para></entry><entry><para>12514</para></entry></row><row><entry><para><ulink url="https://trustbhes.com/">Black Hills Energy Services</ulink>800-215-3035(se habla espanol)</para></entry><entry><para>29032</para></entry></row><row><entry><para><ulink url="http://www.betternegas.com/">CenterPoint Energy Services, Inc.</ulink>888-200-3788(se habla espanol)</para></entry><entry><para>9688</para></entry></row><row><entry><para><ulink url="http://www.woodriverenergy.com/">WoodRiver Energy, LLC</ulink>888-510-9315</para></entry><entry><para>2398</para></entry></row></tbody></tgroup>
    </informaltable>
  </sect1>
  <sect1>
    <title>Supplier marketing and customer contact information</title>
    <para>The natural gas market can be volatile, with available rates changing frequently during the selection period. To give you timely information so you can make the Choice Gas selection that best suits your needs, participating suppliers may contact you by phone, text or email to share their individual offerings. We provide all suppliers with the phone number and email address you may have provided for your Black Hills Energy account.Supplier marketing and customer contact information</para>
    <para>Although we want you to have the chance to receive this additional information from the suppliers, we also understand that calls, texts and emails may be burdensome. Each supplier is limited as to how often they can contact you. If you no longer want to receive these communications from a supplier, request to be removed from their call list or opt out of email communications. After you’ve completed a successful selection, you shouldn’t receive any further contact from suppliers.</para>
  </sect1>
  <sect1>
    <title>Contact us</title>
    <para>For more information about Choice Gas, contact us at <ulink url="tel://8772453506">877-245-3506</ulink>. We are available according to the times and dates listed below.</para>
    <informaltable frame="all">
      <tgroup cols="2"><tbody><row><entry><para>April 10</para></entry><entry><para>8 a.m. – 7:30 p.m. CDT</para></entry></row><row><entry><para>April 13 - April 17</para></entry><entry><para>8 a.m. – 7:30 p.m. CDT</para></entry></row><row><entry><para>April 20 - April 23</para></entry><entry><para>8 a.m. – 7:30 p.m. CDT </para></entry></row></tbody></tgroup>
    </informaltable>
  </sect1>
  <sect1>
    <title>Frequently asked questions</title>
    <sect2 id="accordion-3293">
      <para/>
      <sect3 id="heading-accordion-3293-1">
        <title>Where can I get more information about the 2019-2020 Choice Gas Program and suppliers?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-1">
        <orderedlist>
          <listitem>
            <para><ulink url="https://www.blackhillsenergy.com/sites/blackhillsenergy.com/files/choicegas_ne_guidebook.pdf">Download the guidebook</ulink>. </para>
          </listitem>
          <listitem>
            <para><ulink url="https://www.blackhillsenergy.com/node/362">Click here for more information about the suppliers and their pricing options.</ulink> </para>
          </listitem>
        </orderedlist>
      </sect3>
      <sect3 id="heading-accordion-3293-2">
        <title>How do I select my supplier?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-2">
        <para>You can automatically roll over to your current supplier and pricing option or submit a selection online, through your chosen supplier or by mail.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-3">
        <title>What constitutes a “valid” selection?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-3">
        <para>A selection is considered valid when you submit your choice through one of the accepted submission methods on or before Thursday, April 25, 2019. Confirmation codes are time-sensitive, so check with your supplier about your codes’ expiration date. The first valid selection Black Hills Gas Distribution, LLC receives will be considered your final choice. Record your verification number if you’re submitting your selection online. You’ll need to sign any mailed selection forms for them to be valid.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-4">
        <title>What happens if I move during the Choice Gas program year?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-4">
        <para>If you move from one service address to another, or a new customer moves to a service address within the Choice Gas Program territory, that customer will continue with the supplier previously selected for that address. New construction customers will be mailed a selection packet. For additional questions about service address issues, call 888-890-5554.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-5">
        <title>Does the Choice Gas Program affect the quality of distribution service?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-5">
        <para>No. Regardless of your selection, Black Hills Gas Distribution, LLC will continue to provide meter reading and billing services, respond to gas leaks, and ensure the safety and reliability of the gas supply to Choice Gas Program communities.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-6">
        <title>Does the Choice Gas Program affect distribution charges?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-6">
        <para>No. Changes in distribution rates occur from time to time and are subject to Nebraska Public Service Commission approval.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-7">
        <title>Are the suppliers reliable?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-7">
        <para>Yes. Participating suppliers must meet requirements in Black Hills Gas Distribution, LLC's tariff and approved by the Nebraska Public Service Commission.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-8">
        <title>What if I’m on Budget Billing?</title>
      </sect3>
      <sect3 id="collapse-accordion-3293-8">
        <para>If you’re a Budget Billing customer and select a fixed monthly bill price option a supplier offers, your outstanding Budget Billing balance will be due in full with your June billing.</para>
      </sect3>
    </sect2>
    <sect2>
      <title>Where can I get more information about the 2019-2020 Choice Gas Program and suppliers?</title>
      <sect3 id="collapse-accordion-3293-1">
        <orderedlist>
          <listitem>
            <para><ulink url="https://www.blackhillsenergy.com/sites/blackhillsenergy.com/files/choicegas_ne_guidebook.pdf">Download the guidebook</ulink>. </para>
          </listitem>
          <listitem>
            <para><ulink url="https://www.blackhillsenergy.com/node/362">Click here for more information about the suppliers and their pricing options.</ulink> </para>
          </listitem>
        </orderedlist>
      </sect3>
      <sect3 id="heading-accordion-3293-2">
        <title>How do I select my supplier?</title>
      </sect3>
    </sect2>
    <sect2>
      <title>How do I select my supplier?</title>
      <sect3 id="collapse-accordion-3293-2">
        <para>You can automatically roll over to your current supplier and pricing option or submit a selection online, through your chosen supplier or by mail.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-3">
        <title>What constitutes a “valid” selection?</title>
      </sect3>
    </sect2>
    <sect2>
      <title>What constitutes a “valid” selection?</title>
      <sect3 id="collapse-accordion-3293-3">
        <para>A selection is considered valid when you submit your choice through one of the accepted submission methods on or before Thursday, April 25, 2019. Confirmation codes are time-sensitive, so check with your supplier about your codes’ expiration date. The first valid selection Black Hills Gas Distribution, LLC receives will be considered your final choice. Record your verification number if you’re submitting your selection online. You’ll need to sign any mailed selection forms for them to be valid.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-4">
        <title>What happens if I move during the Choice Gas program year?</title>
      </sect3>
    </sect2>
    <sect2>
      <title>What happens if I move during the Choice Gas program year?</title>
      <sect3 id="collapse-accordion-3293-4">
        <para>If you move from one service address to another, or a new customer moves to a service address within the Choice Gas Program territory, that customer will continue with the supplier previously selected for that address. New construction customers will be mailed a selection packet. For additional questions about service address issues, call 888-890-5554.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-5">
        <title>Does the Choice Gas Program affect the quality of distribution service?</title>
      </sect3>
    </sect2>
    <sect2>
      <title>Does the Choice Gas Program affect the quality of distribution service?</title>
      <sect3 id="collapse-accordion-3293-5">
        <para>No. Regardless of your selection, Black Hills Gas Distribution, LLC will continue to provide meter reading and billing services, respond to gas leaks, and ensure the safety and reliability of the gas supply to Choice Gas Program communities.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-6">
        <title>Does the Choice Gas Program affect distribution charges?</title>
      </sect3>
    </sect2>
    <sect2>
      <title>Does the Choice Gas Program affect distribution charges?</title>
      <sect3 id="collapse-accordion-3293-6">
        <para>No. Changes in distribution rates occur from time to time and are subject to Nebraska Public Service Commission approval.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-7">
        <title>Are the suppliers reliable?</title>
      </sect3>
    </sect2>
    <sect2>
      <title>Are the suppliers reliable?</title>
      <sect3 id="collapse-accordion-3293-7">
        <para>Yes. Participating suppliers must meet requirements in Black Hills Gas Distribution, LLC's tariff and approved by the Nebraska Public Service Commission.</para>
      </sect3>
      <sect3 id="heading-accordion-3293-8">
        <title>What if I’m on Budget Billing?</title>
      </sect3>
    </sect2>
    <sect2>
      <title>What if I’m on Budget Billing?</title>
      <sect3 id="collapse-accordion-3293-8">
        <para>If you’re a Budget Billing customer and select a fixed monthly bill price option a supplier offers, your outstanding Budget Billing balance will be due in full with your June billing.</para>
      </sect3>
      <sect1 id="block-footer-2">
        <para>
          <inlinegraphic fileref="./Nebraska%20Choice%20Gas%20customers%20_%20Black%20Hills%20Energy_files/bhe-white-logo.svg" width="0.7862inch" depth="0.3929inch"/>
        </para>
        <para><ulink url="https://careers.blackhillsenergy.com/">CAREERS</ulink> <ulink url="https://www.blackhillsenergy.com/form/contact-customer-service">CONTACT US</ulink> <ulink url="http://ir.blackhillscorp.com/corporateprofile.aspx?iid=4010420">INVESTOR RELATIONS</ulink><ulink url="https://www.blackhillsenergy.com/node/635">NEWS/BLOG</ulink> <ulink url="https://www.blackhillsenergy.com/privacy-policy">PRIVACY</ulink> <ulink url="https://www.blackhillsenergy.com/terms-use">TERMS OF USE</ulink></para>
        <para>Black Hills Energy is a part of <ulink url="https://www.blackhillscorp.com/">Black Hills Corporation</ulink> </para>
        <para>Copyright © 2020 Black Hills Energy</para>
        <para>
          <inlinegraphic fileref="./Nebraska%20Choice%20Gas%20customers%20_%20Black%20Hills%20Energy_files/facebook.png" width="0.8071inch" depth="0.4138inch"/>
        </para>
        <para>
          <inlinegraphic fileref="./Nebraska%20Choice%20Gas%20customers%20_%20Black%20Hills%20Energy_files/twitter.png" width="0.8071inch" depth="0.4138inch"/>
        </para>
        <para>
          <inlinegraphic fileref="./Nebraska%20Choice%20Gas%20customers%20_%20Black%20Hills%20Energy_files/instagram.png" width="0.8071inch" depth="0.4138inch"/>
        </para>
        <para>
          <inlinegraphic fileref="./Nebraska%20Choice%20Gas%20customers%20_%20Black%20Hills%20Energy_files/linkedin.png" width="0.8071inch" depth="0.4138inch"/>
        </para>
        <para>
          <inlinegraphic fileref="./Nebraska%20Choice%20Gas%20customers%20_%20Black%20Hills%20Energy_files/youtube.png" width="0.8071inch" depth="0.4138inch"/>
        </para>
      </sect1>
      <para>window.mdc.autoInit();//&lt;![CDATA[

pagespeed.addInstrumentationInit('/mod_pagespeed_beacon', 'load', '', 'https://www.blackhillsenergy.com/services/choice-gas-program/nebraska-choice-gas-customers');
//]]&gt;!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","1147193305334821");fbq("set","agent","tmgoogletagmanager","1147193305334821");fbq("track","PageView");<note><remark>HTML: &lt;noscript&gt;</remark></note><inlinegraphic fileref="https://www.facebook.com/tr?id=1147193305334821&amp;ev=PageView&amp;noscript=1" width="0.0161inch" depth="0.0161inch"/><note><remark>HTML: &lt;/noscript&gt;</remark></note> !function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","477515563062837");fbq("track","PageView");<note><remark>HTML: &lt;noscript&gt;</remark></note><inlinegraphic fileref="https://www.facebook.com/tr?id=477515563062837&amp;ev=PageView&amp;noscript=1" width="0.0161inch" depth="0.0161inch"/><note><remark>HTML: &lt;/noscript&gt;</remark></note> </para>
      <sect1 id="batBeacon0.6137131948796937">
        <para>
          <inlinegraphic fileref="./Nebraska%20Choice%20Gas%20customers%20_%20Black%20Hills%20Energy_files/0" width="0.0161inch" depth="0.0161inch"/>
          <anchor id="batBeacon0.08048479298296507"/>
        </para>
      </sect1>
      <para/>
      <sect1 id="_hj_feedback_container">
        <para/>
        <sect2 id="_hj-f5b2a1eb-9b07_feedback">
          <para>
            <note>
              <remark>Minimized State</remark>
            </note>
          </para>
          <sect3 id="_hj-f5b2a1eb-9b07_feedback_minimized">
            <para>Feedback </para>
            <sect4 id="_hj-f5b2a1eb-9b07_feedback_minimized_message">
              <para><anchor id="_hj-f5b2a1eb-9b07_feedback_minimized_text_initial"/>Help us improve by sharing your feedback. <anchor id="_hj-f5b2a1eb-9b07_feedback_minimized_text_thankyou"/>Thank you for sharing your feedback with us! </para>
            </sect4>
          </sect3>
          <sect3 id="_hj-f5b2a1eb-9b07_feedback_open">
            <para>
              <anchor id="_hj-f5b2a1eb-9b07_feedback_open_close_phone"/>
              <note>
                <remark>Opened State</remark>
              </note>
              <note>
                <remark>STEP 1: EMOTION</remark>
              </note>
            </para>
            <sect4 id="_hj-f5b2a1eb-9b07_state-1">
              <para>How would you rate your overall experience on BlackHillsEnergy.com?</para>
              <para>Hate </para>
              <para>Dislike </para>
              <para>Neutral </para>
              <para>Like </para>
              <para>Love </para>
              <sect5 id="_hj-f5b2a1eb-9b07_toolset_action_select">
                <para>Select an element on the page.</para>
              </sect5>
            </sect4>
            <sect4 id="_hj-f5b2a1eb-9b07_state-2">
              <para><note><remark>STEP 2: EMAIL</remark></note>false</para>
            </sect4>
            <sect4 id="_hj-f5b2a1eb-9b07_state-3">
              <para><note><remark>STEP 3: THANK YOU AND CONSENT</remark></note>Thank you for sharing your feedback with us!</para>
              <para>Connecting your feedback with data related to your visits (device-specific, usage data, cookies, behavior and interactions) will help us improve faster. Do you give us your consent to do so for your previous and future visits? <ulink url="https://www.hotjarconsent.com/">More information</ulink></para>
            </sect4>
            <para><note><remark>FOOTER</remark></note>Skip Send </para>
          </sect3>
          <sect3 id="_hj-f5b2a1eb-9b07_feedback_page_highlight">
            <para>
              <note>
                <remark>PAGE HIGHLIGHTER</remark>
              </note>
            </para>
            <sect4 id="_hj-f5b2a1eb-9b07_feedback_page_highlight_line_top">
              <para/>
            </sect4>
            <sect4 id="_hj-f5b2a1eb-9b07_feedback_page_highlight_line_right">
              <para/>
            </sect4>
            <sect4 id="_hj-f5b2a1eb-9b07_feedback_page_highlight_line_bottom">
              <para/>
            </sect4>
            <sect4 id="_hj-f5b2a1eb-9b07_feedback_page_highlight_line_left">
              <para/>
            </sect4>
            <sect4 id="_hj-f5b2a1eb-9b07_feedback_top_message_select">
              <para>Select an element on the page. <anchor id="_hj-f5b2a1eb-9b07_feedback_top_message_select_close"/></para>
            </sect4>
          </sect3>
          <sect3 id="_hj-f5b2a1eb-9b07_feedback_content_dimmer_top">
            <para>
              <note>
                <remark>DIMMERS (OVERLAY) + ELEMENT HIGHLIGHTER</remark>
              </note>
            </para>
          </sect3>
          <sect3 id="_hj-f5b2a1eb-9b07_feedback_content_dimmer_right">
            <para/>
          </sect3>
          <sect3 id="_hj-f5b2a1eb-9b07_feedback_content_dimmer_bottom">
            <para/>
          </sect3>
          <sect3 id="_hj-f5b2a1eb-9b07_feedback_content_dimmer_left">
            <para/>
          </sect3>
          <sect3 id="_hj-f5b2a1eb-9b07_feedback_content_highlighter">
            <para>
              <anchor id="_hj-f5b2a1eb-9b07_feedback_content_highlighter_close"/>
            </para>
          </sect3>
        </sect2>
      </sect1>
      <sect1 id="KampyleAnimationContainer">
        <para/>
      </sect1>
    </sect2>
  </sect1>
</article>

 """

dataroot = etree.XML(myxml)
#  this returns the root
print(dataroot.tag, type(dataroot.tag))
for elements in dataroot.iter("title"):
    print(elements.text)
