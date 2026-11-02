/* Agent Base demo scene for the BL Agency site. Simulated activity, no real data. */
(function(){
const stage=document.getElementById('ab-stage'); if(!stage||!window.THREE) return;
const canvas=stage.querySelector('canvas');
const rand=(a,b)=>a+Math.random()*(b-a), pick=a=>a[Math.floor(Math.random()*a.length)];
const hex=c=>'#'+c.toString(16).padStart(6,'0');
const still=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true});
renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));
renderer.shadowMap.enabled=true; renderer.shadowMap.type=THREE.PCFSoftShadowMap;
renderer.outputEncoding=THREE.sRGBEncoding;
const scene=new THREE.Scene(); scene.fog=new THREE.Fog(0xd98f5f,45,110);
const camera=new THREE.PerspectiveCamera(40,1,.1,300); camera.position.set(15,17,19);
const controls=new THREE.OrbitControls(camera,renderer.domElement);
controls.enableDamping=true; controls.dampingFactor=.08; controls.enablePan=false; controls.enableZoom=false;
controls.target.set(0,.5,0); controls.maxPolarAngle=Math.PI*.44; controls.autoRotate=!still; controls.autoRotateSpeed=.4;
controls.addEventListener('start',()=>{controls.autoRotate=false;});

scene.add(new THREE.HemisphereLight(0xffe9cf,0x6b3a22,.6));
const sun=new THREE.DirectionalLight(0xfff4e6,.85); sun.position.set(12,22,8); sun.castShadow=true;
sun.shadow.mapSize.set(1024,1024); Object.assign(sun.shadow.camera,{left:-16,right:16,top:16,bottom:-16,near:1,far:60}); scene.add(sun);
const mat=(c,o)=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.65,metalness:.05},o||{}));
function mesh(g,m,x,y,z,p){const o=new THREE.Mesh(g,m);o.position.set(x||0,y||0,z||0);o.castShadow=true;o.receiveShadow=true;(p||scene).add(o);return o;}
const ground=mesh(new THREE.CircleGeometry(120,64),mat(0xb8703f,{roughness:1})); ground.rotation.x=-Math.PI/2; ground.castShadow=false;

const R=3.2,D=R*Math.sqrt(3)*1.03,TOP=.46,white=0xf4efe6;
const ZONES=[{id:'research',name:'Research',color:0x5b8def},{id:'write',name:'Writing',color:0x9b6bff},{id:'review',name:'Human review',color:0xf2c14e},
  {id:'outbox',name:'Outbox',color:0x3fc1a5},{id:'replies',name:'Replies',color:0xff8a5b},{id:'meetings',name:'Meetings',color:0x7bd389}];
const Z={};
function tile(p,c,hq){mesh(new THREE.CylinderGeometry(R,R,.34,6),mat(c,{emissive:c,emissiveIntensity:.35}),p.x,.17,p.z);
  mesh(new THREE.CylinderGeometry(R*.93,R*.93,.42,6),mat(hq?0x3d3552:0x4b505f,{roughness:.9}),p.x,.25,p.z);}
tile(new THREE.Vector3(),0xff5d8f,true);
ZONES.forEach((z,i)=>{const a=(30+60*i)*Math.PI/180;z.out=new THREE.Vector3(Math.sin(a),0,Math.cos(a));z.perp=new THREE.Vector3(z.out.z,0,-z.out.x);
  z.pos=z.out.clone().multiplyScalar(D);Z[z.id]=z;tile(z.pos,z.color);});
function spot(id){if(id==='hq'){const t=Math.random()*Math.PI*2,r=rand(1.9,2.4);return new THREE.Vector3(Math.cos(t)*r,TOP,Math.sin(t)*r);}
  const z=Z[id],p=z.pos.clone().addScaledVector(z.out,-.7),r=Math.random()*.9,t=Math.random()*Math.PI*2;p.x+=Math.cos(t)*r;p.z+=Math.sin(t)*r;p.y=TOP;return p;}
const bpos=(z,k)=>z.pos.clone().addScaledVector(z.out,R*(k||.38));
(function(){
  let z=Z.research,p=bpos(z),g=new THREE.Group();g.position.copy(p);scene.add(g);
  mesh(new THREE.CylinderGeometry(.9,1.1,1.1,16),mat(white),0,TOP+.55,0,g);
  const dish=mesh(new THREE.SphereGeometry(1.05,24,12,0,Math.PI*2,0,Math.PI/2.4),mat(z.color,{side:THREE.DoubleSide}),0,TOP+1.7,0,g);dish.rotation.x=Math.PI*.8;dish.rotation.z=.3;z.spin=g;
  z=Z.write;p=bpos(z);mesh(new THREE.BoxGeometry(2,1.3,1.5),mat(white),p.x,TOP+.65,p.z).rotation.y=Math.atan2(z.out.x,z.out.z);
  for(let i=-1;i<=1;i++){const q=p.clone().addScaledVector(z.perp,i*.6).addScaledVector(z.out,-.76);const w=mesh(new THREE.BoxGeometry(.42,.5,.05),mat(0x2a2f6b,{emissive:z.color,emissiveIntensity:.6}),q.x,TOP+.8,q.z);w.rotation.y=Math.atan2(z.out.x,z.out.z);}
  z=Z.review;p=bpos(z,.15);const gg=new THREE.Group();gg.position.copy(p);gg.rotation.y=Math.atan2(z.perp.x,z.perp.z);scene.add(gg);
  mesh(new THREE.BoxGeometry(.45,2.2,.45),mat(white),-1.1,TOP+1.1,0,gg);mesh(new THREE.BoxGeometry(.45,2.2,.45),mat(white),1.1,TOP+1.1,0,gg);
  mesh(new THREE.BoxGeometry(2.8,.45,.6),mat(z.color,{emissive:z.color,emissiveIntensity:.4}),0,TOP+2.35,0,gg);
  z.lamp=mesh(new THREE.SphereGeometry(.2,12,10),mat(0xffe08a,{emissive:0xffc93c,emissiveIntensity:1}),0,TOP+2.8,0,gg);
  z=Z.outbox;p=bpos(z);mesh(new THREE.CylinderGeometry(.75,1,2.6,8),mat(white),p.x,TOP+1.3,p.z);mesh(new THREE.CylinderGeometry(.85,.85,.3,8),mat(z.color),p.x,TOP+2.1,p.z);
  z.beacon=mesh(new THREE.SphereGeometry(.16,10,8),mat(z.color,{emissive:z.color,emissiveIntensity:1}),p.x,TOP+3.85,p.z);z.top=new THREE.Vector3(p.x,TOP+3.9,p.z);
  mesh(new THREE.CylinderGeometry(.04,.04,1.2),mat(0x777777),p.x,TOP+3.2,p.z);
  z=Z.replies;p=bpos(z);mesh(new THREE.CylinderGeometry(1.1,1.2,1,16),mat(white),p.x,TOP+.5,p.z);mesh(new THREE.SphereGeometry(.95,20,10,0,Math.PI*2,0,Math.PI/2),mat(z.color),p.x,TOP+1,p.z);
  z=Z.meetings;p=bpos(z,.3);mesh(new THREE.CylinderGeometry(1.5,1.6,.35,24),mat(white),p.x,TOP+.17,p.z);
  z.dome=mesh(new THREE.SphereGeometry(1.4,28,14,0,Math.PI*2,0,Math.PI/2),mat(z.color,{transparent:true,opacity:.75,emissive:z.color,emissiveIntensity:.2,roughness:.2}),p.x,TOP+.35,p.z);
  mesh(new THREE.CylinderGeometry(1.4,1.6,.5,6),mat(white),0,TOP+.25,0);mesh(new THREE.CylinderGeometry(.06,.06,2.6),mat(0x888888),0,TOP+1.6,0);
  Z.hqFlag=mesh(new THREE.BoxGeometry(1,.6,.04),mat(0xff5d8f,{emissive:0xff5d8f,emissiveIntensity:.3}),.5,TOP+2.6,0);
})();
const rocks=[];
for(let i=0;i<22;i++){const a=Math.random()*Math.PI*2,r=rand(15,36);const m=mesh(new THREE.DodecahedronGeometry(rand(.3,1.1)),mat(0x6e4a38,{flatShading:true}),Math.cos(a)*r,rand(5,15),Math.sin(a)*r);m.castShadow=false;rocks.push({m,y:m.position.y,s:rand(.3,.8),p:Math.random()*6});}
for(let i=0;i<26;i++){const a=Math.random()*Math.PI*2,r=rand(10.5,30);mesh(new THREE.DodecahedronGeometry(rand(.15,.6)),mat(0xa86b45,{flatShading:true}),Math.cos(a)*r,.05,Math.sin(a)*r).rotation.set(Math.random(),Math.random(),0);}

/* zone labels */
const labelsEl=stage.querySelector('.ab-labels');
const labels=ZONES.map(z=>{const el=document.createElement('div');el.className='ab-zl';el.innerHTML=`<i style="background:${hex(z.color)}"></i>${z.name}`;labelsEl.appendChild(el);return{el,pos:z.pos.clone().addScaledVector(z.out,R*1.05),y:.5};});
(function(){const el=document.createElement('div');el.className='ab-zl';el.innerHTML='<i style="background:#ff5d8f"></i>Agent Base manager';labelsEl.appendChild(el);labels.push({el,pos:new THREE.Vector3(),y:3.5});})();

/* agents */
function bot(color){const g=new THREE.Group();
  mesh(new THREE.CylinderGeometry(.22,.28,.5,14),mat(white),0,.35,0,g);mesh(new THREE.CylinderGeometry(.29,.29,.1,14),mat(color),0,.2,0,g);
  mesh(new THREE.SphereGeometry(.26,16,12),mat(white),0,.78,0,g);mesh(new THREE.BoxGeometry(.32,.11,.1),mat(0x1d2433,{emissive:color,emissiveIntensity:.9}),0,.8,.21,g);
  mesh(new THREE.CylinderGeometry(.015,.015,.24),mat(0x888888),0,1.12,0,g);
  const tip=mesh(new THREE.SphereGeometry(.065,8,8),mat(color,{emissive:color,emissiveIntensity:1}),0,1.25,0,g);
  const crate=mesh(new THREE.BoxGeometry(.34,.26,.34),mat(color,{emissive:color,emissiveIntensity:.2}),0,1.5,0,g);crate.visible=false;return{g,tip,crate};}
class Agent{constructor(s){Object.assign(this,s);const b=bot(s.color);Object.assign(this,b);scene.add(this.g);this.g.position.copy(spot(s.home));
    this.state='idle';this.busy=false;this.cool=rand(.5,2);this.ph=Math.random()*6;
    if(s.human){this.g.scale.setScalar(1.3);mesh(new THREE.TorusGeometry(.29,.035,8,20,Math.PI),mat(0x2b2b33),0,.8,0,this.g);}}
  work(t,cb){this.state='working';this.timer=t;this.onDone=cb;}
  walk(p,cb){this.state='walking';this.target=p;this.onArrive=cb;}
  update(dt){const p=this.g.position;
    if(this.state==='walking'){this.ph+=dt*11;const dx=this.target.x-p.x,dz=this.target.z-p.z,L=Math.hypot(dx,dz),st=2.4*dt;
      if(L<=st){p.x=this.target.x;p.z=this.target.z;this.state='idle';const c=this.onArrive;this.onArrive=null;c&&c();}else{p.x+=dx/L*st;p.z+=dz/L*st;this.g.rotation.y=Math.atan2(dx,dz);}
      p.y=TOP+Math.abs(Math.sin(this.ph))*.09;}
    else if(this.state==='working'){this.ph+=dt*4;this.timer-=dt;p.y=TOP+Math.sin(this.ph*2)*.03;this.tip.material.emissiveIntensity=1.1+Math.sin(this.ph*5)*.9;
      if(this.timer<=0){this.state='idle';this.tip.material.emissiveIntensity=1;const c=this.onDone;this.onDone=null;c&&c();}}
    else{p.y=TOP;if(!this.busy){this.cool-=dt;if(this.cool<=0){this.cool=rand(2.5,5);if(Math.random()<.5)this.walk(spot(this.home));else this.work(rand(1.5,3));}}}}}
const A={};
[{key:'mgr',name:'Agent Base manager',home:'hq',color:0xff5d8f,human:true},{key:'Scout',name:'Scout',home:'research',color:0x5b8def},{key:'Lens',name:'Lens',home:'research',color:0x4fd1e8},
 {key:'Quill',name:'Quill',home:'write',color:0x9b6bff},{key:'Relay',name:'Relay',home:'outbox',color:0x3fc1a5},{key:'Echo',name:'Echo',home:'replies',color:0xff8a5b},{key:'Atlas',name:'Atlas',home:'meetings',color:0x7bd389}]
 .forEach(s=>A[s.key]=new Agent(s));
const all=Object.values(A);

const envs=[];let pulse=0;
function envelope(from,to,arc,dur,fade,cb){const m=mesh(new THREE.BoxGeometry(.42,.05,.3),mat(0xffffff,{emissive:0xffffff,emissiveIntensity:.4,transparent:true}),from.x,from.y,from.z);
  m.castShadow=false;envs.push({m,from:from.clone(),to:to.clone(),arc,dur,fade,t:0,cb});}

/* simulated pipeline: generic accounts, no real names */
const ACCOUNTS=['a 40 person SaaS team','a fintech in Austin','a staffing firm in Chicago','a B2B agency in Denver','a consulting firm in Boston','a SaaS startup in Miami','a services firm in Atlanta'];
const k={leads:0,sent:0,replies:0,meetings:0};
const kEl={};['leads','sent','replies','meetings'].forEach(n=>kEl[n]=document.querySelector('[data-k="'+n+'"]'));
const nowEl=stage.querySelector('.ab-now span'),dotEl=stage.querySelector('.ab-now i');
function say(color,html){nowEl.innerHTML=html;dotEl.style.background=color;}
function bump(n){k[n]++;kEl[n].textContent=k[n];}
const queue=[];
function cycle(){const acc=pick(ACCOUNTS);const replied=Math.random()<.45,meet=replied&&Math.random()<.6;
  queue.push(['lead',acc],['preview',acc],['draft',acc],['approve',acc],['send',acc]);if(replied)queue.push(['reply',acc]);if(meet)queue.push(['meet',acc]);}
function step(){
  if(!queue.length)cycle();
  const [t,acc]=queue[0];const done=a=>()=>{a.busy=false;a.cool=rand(1.5,3);};
  const take=a=>{if(a.busy)return false;a.busy=true;queue.shift();return true;};
  switch(t){
    case'lead':{const a=A.Scout;if(!take(a))return;say('#5b8def',`<b>Scout</b> found ${acc} hiring its first SDR`);
      a.walk(spot('research'),()=>a.work(1.8,()=>{bump('leads');a.crate.visible=true;a.walk(spot('write'),()=>{a.crate.visible=false;a.walk(spot('research'),done(a));});}));break;}
    case'preview':{const a=A.Lens;if(!take(a))return;say('#4fd1e8',`<b>Lens</b> is researching ${acc}'s market`);a.walk(spot('research'),()=>a.work(2.2,done(a)));break;}
    case'draft':{const a=A.Quill;if(!take(a))return;say('#9b6bff',`<b>Quill</b> is writing to ${acc}`);
      a.walk(spot('write'),()=>a.work(2.2,()=>{a.crate.visible=true;a.walk(spot('review'),()=>{a.crate.visible=false;a.walk(spot('write'),done(a));});}));break;}
    case'approve':{const a=A.mgr;if(!take(a))return;say('#f2c14e',`<b>Agent Base manager</b> is reviewing the email to ${acc}`);
      a.walk(spot('review'),()=>a.work(2.2,()=>{say('#f2c14e',`<b>Agent Base manager</b> approved the email to ${acc}`);a.walk(spot('hq'),done(a));}));break;}
    case'send':{const a=A.Relay;if(!take(a))return;say('#3fc1a5',`<b>Relay</b> sent the email to ${acc}`);
      a.walk(spot('outbox'),()=>a.work(1.4,()=>{const z=Z.outbox;bump('sent');envelope(z.top,z.top.clone().addScaledVector(z.out,9).add(new THREE.Vector3(0,10,0)),2,2.2,true);done(a)();}));break;}
    case'reply':{const a=A.Echo;if(!take(a))return;const z=Z.replies,to=bpos(z).add(new THREE.Vector3(0,2.2,0));say('#ff8a5b',`<b>Echo</b> got a reply from ${acc}`);
      envelope(to.clone().add(new THREE.Vector3(0,9,0)).addScaledVector(z.out,6),to,1,1.8,false,()=>{bump('replies');a.work(2,done(a));});break;}
    case'meet':{const a=A.Atlas;if(!take(a))return;say('#7bd389',`<b>Atlas</b> booked a meeting with ${acc}`);
      a.walk(spot('meetings'),()=>a.work(2,()=>{bump('meetings');pulse=1.6;done(a)();}));break;}
  }
}

function resize(){const w=stage.clientWidth,h=stage.clientHeight;renderer.setSize(w,h,false);camera.aspect=w/h;
  camera.position.setLength(w<640?38:28);camera.updateProjectionMatrix();}
window.addEventListener('resize',resize);resize();
const v=new THREE.Vector3();
function placeLabels(){const w=stage.clientWidth,h=stage.clientHeight;labels.forEach(l=>{v.copy(l.pos);v.y=l.y;v.project(camera);
  const vis=v.z<1;l.el.style.display=vis?'flex':'none';l.el.style.transform=`translate(${(v.x*.5+.5)*w}px,${(-v.y*.5+.5)*h}px) translate(-50%,-50%)`;});}

let visible=false,last=performance.now(),next=1,t=0;
new IntersectionObserver(es=>{visible=es[0].isIntersecting;last=performance.now();},{threshold:.1}).observe(stage);
function frame(now){requestAnimationFrame(frame);if(!visible&&!still)return;
  const dt=Math.min((now-last)/1000,.05);last=now;t+=dt;
  if(!still){next-=dt;if(next<=0){step();next=rand(.9,1.6);}
    all.forEach(a=>a.update(dt));
    if(Z.research.spin)Z.research.spin.rotation.y+=dt*.6;
    Z.outbox.beacon.material.emissiveIntensity=.6+Math.sin(t*4)*.5;Z.review.lamp.material.emissiveIntensity=.7+Math.sin(t*3)*.4;Z.hqFlag.rotation.y=Math.sin(t*1.5)*.25;
    if(pulse>0){pulse-=dt;Z.meetings.dome.scale.setScalar(1+Math.max(pulse,0)*.12);}
    rocks.forEach(r=>{r.m.position.y=r.y+Math.sin(t*r.s+r.p)*.4;r.m.rotation.y+=dt*.1;});
    for(let i=envs.length-1;i>=0;i--){const e=envs[i];e.t+=dt/e.dur;const u=Math.min(e.t,1);e.m.position.lerpVectors(e.from,e.to,u);e.m.position.y+=Math.sin(u*Math.PI)*e.arc;e.m.rotation.y+=dt*4;
      if(e.fade)e.m.material.opacity=1-u;if(u>=1){scene.remove(e.m);envs.splice(i,1);e.cb&&e.cb();}}}
  controls.update();renderer.render(scene,camera);placeLabels();}
requestAnimationFrame(frame);
if(still){visible=true;say('#f2c14e','<b>Agent Base manager</b> reviews every email before it goes out');}
})();
