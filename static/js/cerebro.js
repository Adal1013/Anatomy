	var scene = new THREE.Scene();

	var container = document.getElementById('canvas');
	var w = container.offsetWidth;
	var h = container.offsetHeight;

	const aspectRatio = w / h;
	var camera = new THREE.PerspectiveCamera(75,aspectRatio,0.1,100);

	camera.position.z = 6;
	camera.position.x = 0;
	camera.position.y = 0;

	var renderer = new THREE.WebGLRenderer();
	renderer.setSize(w, h);
	container.appendChild(renderer.domElement);

  	function loadModel() {
		object.traverse( function ( child ) {
			if ( child.isMesh ) child.material.map = texture;
		} );
		object.position.y = -3;
		scene.add( object );
	}

	var manager = new THREE.LoadingManager( loadModel );
	manager.onProgress = function ( item, loaded, total ) {
		console.log( item, loaded, total );
	};

	var textureLoader = new THREE.TextureLoader( manager );
	var texture = textureLoader.load( urltex);
	function onProgress( xhr ) {
		if ( xhr.lengthComputable ) {
			var percentComplete = xhr.loaded / xhr.total * 100;
			console.log( 'model ' + Math.round( percentComplete, 2 ) + '% downloaded' );
		}
	}
	
	function onError( xhr ) {}
	var loader = new THREE.OBJLoader( manager );
	loader.load( urlobj, function ( obj ) {
		object = obj;
	}, onProgress, onError );

	var ambientLight = new THREE.AmbientLight( 0xcccccc, 0.4 );
	scene.add( ambientLight );
	var pointLight = new THREE.PointLight( 0xffffff, 0.8 );
	camera.add( pointLight );
	scene.add( camera );
	scene.background = new THREE.Color(0xeeeeee);

	var controls = new THREE.OrbitControls(camera,renderer.domElement);

	function loop(){
		requestAnimationFrame(loop);
		renderer.render(scene,camera);
	}

	loop();
