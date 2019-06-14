$tag = "dev-" + (Get-Date -UFormat "%y%m%d%H%M%S")

Function BuildImage
{
	param([string]$Dockerfile, [string]$ImageName )

	docker build -t "${imageName}:${tag}" -f ./$Dockerfile .
	docker tag "${imageName}:${tag}" "${imageName}:latest-dev"
}

BuildImage "Dockerfile.response" "protolabs/response"
BuildImage "Dockerfile.cron" "protolabs/response-cron"